from umqtt.simple import MQTTClient

username = ""
password = ""
broker_hostname = ""
broker_port = 1883
topic = ""
device_id = ""

def publish(moisture_value):
    client = MQTTClient(
        device_id,
        broker_hostname,
        user=username,
        password=password,
        port=broker_port
        )
    client.connect()
    client.publish(topic=topic, msg=str(moisture_value))
    client.disconnect()
