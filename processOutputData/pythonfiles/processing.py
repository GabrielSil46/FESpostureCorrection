from neurolabkit.mqtt import MQTTServiceManager
from neurolabkit.mqtt.logging import logger
import threading



processing = MQTTServiceManager(
            service_description="Simple service to simulate a person's walk",
            service_id="2345",
            hostname='10.1.0.18',
            port = 1883,
        )

def processData(data):
    output_data = data
    processing.publish(processing.stream_topic, output_data)
    print(output_data)

processing.add_listener(processData)

processing.connect()


