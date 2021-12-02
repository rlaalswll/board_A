import paho.mqtt.client as mqtt
topic = "deviceid/mj/angle"
server = "3.84.34.84"

def on_connect(client, userdata, flags, rc):
    print("Connected with RC : " + str(rc))
    client.subscribe(topic)

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload.decode('UTF-8')))

client = mqtt.Client()
client.connect(server, 1883, 60)
client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()