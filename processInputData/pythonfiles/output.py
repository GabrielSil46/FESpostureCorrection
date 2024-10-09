from neurolabkit.mqtt import MQTTServiceManager
from neurolabkit.mqtt.logging import logger
import threading

def tesFunction(data):
    print(data)


output = MQTTServiceManager(
            service_description="Simple service to simulate a person's walk",
            service_id="2345",
            service_type="output",
            hostname='10.1.0.18',
            port = 1883,
        )

output.add_listener(tesFunction)

output.connect()


