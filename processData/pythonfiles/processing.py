from neurolabkit.mqtt import MQTTServiceManager
from neurolabkit.mqtt.logging import logger
import threading



processing = MQTTServiceManager(
            service_description="Processing (accepts points string as input, outputs FES voltage duty cycle)",
            service_id="2345",
            hostname='127.0.0.1',
            port = 1883,
        )

def processData(data):
    output_data = data.decode('utf8')
    processing.publish(processing.stream_topic, output_data)
    print(output_data)

processing.add_listener(processData)

processing.connect()


