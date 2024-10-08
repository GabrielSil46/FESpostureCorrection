from neurolabkit.mqtt import MQTTServiceManager
from neurolabkit.mqtt.logging import logger
import threading

def tesFunction(data):
    print(data)

input = MQTTServiceManager(
            service_description="Simple service to simulate a person's walk",
            service_id="1234",
            service_type="input",
            hostname='10.1.0.18',
            port = 1883,
        )
input.add_service(tesFunction)

input.connect()


