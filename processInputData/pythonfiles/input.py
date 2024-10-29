from neurolabkit.mqtt import MQTTServiceManager
from neurolabkit.mqtt.logging import logger
import threading
import mediapipe as mp
import cv2
import math

input = MQTTServiceManager(
            service_description="Mediapipe (pega input da câmera, ângulo até a postura correta como output)",
            service_id="1234",
            service_type="input",
            hostname='127.0.0.1',
            port = 1883,
        )

def spine_calculation(data):

    def calcular_angulo(p1, p2, p3):
        delta1_x, delta1_y = p1[0] - p2[0], p1[1] - p2[1]
        delta2_x, delta2_y = p3[0] - p2[0], p3[1] - p2[1]
        produto_escalar = (delta1_x * delta2_x + delta1_y * delta2_y)
        comprimento1 = math.sqrt(delta1_x ** 2 + delta1_y ** 2)
        comprimento2 = math.sqrt(delta2_x ** 2 + delta2_y ** 2)
        cos_angulo = produto_escalar / (comprimento1 * comprimento2)
        angulo = math.degrees(math.acos(cos_angulo))
        mp_pose = mp.solutions.pose

    # Iniciar captura
    cap = cv2.VideoCapture(0)
        
    mp_pose = mp.solutions.pose
    with mp_pose.Pose(min_detection_confidence=0.7, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            success, frame = cap.read()
            if not success:
                print("Ignorando frame vazio.")
                continue

            # Converte a imagem para RGB
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False

            # Processa a imagem e detecta a pose
            results = pose.process(image)

            # Converte a imagem de volta para BGR para exibir com OpenCV
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            # Verifica se há algum corpo detectado
            if results.pose_landmarks:
                landmarks = results.pose_landmarks.landmark
                ombro = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                        landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                quadril = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,
                        landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
                orelha = [landmarks[mp_pose.PoseLandmark.RIGHT_EAR.value].x,
                        landmarks[mp_pose.PoseLandmark.RIGHT_EAR.value].y]

                h, w, c = image.shape
                ombro_coordenadas = (int(ombro[0] * w), int(ombro[1] * h))
                quadril_coordenadas = (int(quadril[0] * w), int(quadril[1] * h))
                orelha_coordenadas = (int(orelha[0] * w), int(orelha[1] * h))

                # Desenha os pontos do ombro, quadril e orelha
                cv2.circle(image, ombro_coordenadas, 10, (0, 255, 0), -1)
                cv2.circle(image, quadril_coordenadas, 10, (0, 255, 0), -1)
                cv2.circle(image, orelha_coordenadas, 10, (0, 255, 0), -1)

                # Conecta os três pontos com linhas
                cv2.line(image, quadril_coordenadas, ombro_coordenadas, (0, 255, 0), 3)
                cv2.line(image, ombro_coordenadas, orelha_coordenadas, (0, 255, 0), 3)

                # Calcula o ângulo da postura (entre quadril, ombro e orelha)
                angulo = calcular_angulo(quadril, ombro, orelha)

                # Calcula a diferença para 180 graus (postura ereta)
                diferenca_angulo = (180 - angulo)

                # Modula o valor do 3º canal do MQTT com base no ângulo
                valor_canal_3 = max(0, min(100, 100 - abs(diferenca_angulo)))  # Ajusta o valor entre 0 e 100
                # enviar_dados_mqtt(valor_canal_3)  # Envia o valor para o MQTT

                # Imprime a diferença no terminal em tempo real
                print(f"Falta: {diferenca_angulo:.2f}° para postura ereta")

                # Exibe a diferença para o ângulo postural ideal na parte inferior do vídeo
                cv2.putText(image, f'Faltam: {int(diferenca_angulo)}° para postura ideal',
                            (20, image.shape[0] - 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

                # Se a postura estiver ereta (ângulo próximo de 180 graus), emite o beep
                # if 175 <= angulo <= 185:
                #     emitir_beep_thread()

            # Mostra o vídeo com os pontos rastreados e o ângulo
            cv2.imshow('Postura Correta', image)

            if cv2.waitKey(5) & 0xFF == 27:  # Pressione 'ESC' para sair
                break
                
    data = valor_canal_3
    input.publish(input.stream_topic, data)
    print(data)

input.add_service(spine_calculation)

input.connect()

