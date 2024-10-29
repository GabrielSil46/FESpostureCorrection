from neurolabkit.mqtt import MQTTServiceManager
from neurolabkit.mqtt.logging import logger
import threading

filterd_dutycycle = 0

def output_to_FES(data):
    # Filtra os dados e gera um duty cycle para o FES (entre 0 e 1)
    filtered_dutycycle = min(1, filtered_dutycycle + 1/30 * data/100)

    # enviar dados para o FES via MQTT

    logger.info("Data was: " + data.decode('utf8'))


output = MQTTServiceManager(
            service_description="FES Controller (accepts duty cycle as input, outputs it to FES via MQTT)",
            service_id="6789",
            service_type="output",
            hostname='127.0.0.1',
            port = 1883,
        )

output.add_listener(output_to_FES)

output.connect()


