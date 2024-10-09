from neurolabkit.mqtt import MQTTServiceManager
from neurolabkit.mqtt.logging import logger
import threading

def tesFunction(data):
    logger.info("Data was: " + data.decode('utf8'))


output = MQTTServiceManager(
            service_description="Simple service to simulate a person's walk (output)",
            service_id="6789",
            service_type="output",
            hostname='10.1.0.18',
            port = 1883,
        )

output.add_listener(tesFunction)

output.connect()


