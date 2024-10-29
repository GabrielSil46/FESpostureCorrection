from neurolabkit.mqtt import MQTTServiceManager
from neurolabkit.mqtt.logging import logger
import threading

input = MQTTServiceManager(
            service_description="Simple service to simulate a person's walk",
            service_id="1234",
            service_type="input",
            hostname='127.0.0.1',
            port = 1883,
        )

def tesFunction(data):
    input.publish(input.stream_topic, "[1,2,3,4]")
    print(data)

input.add_service(tesFunction)

input.connect()


