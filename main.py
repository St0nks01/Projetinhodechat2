import paho.mqtt.client as mqtt

def ao_conectar(client,userdata,flags, rc):
    print("Nos conectamos com o seguinte código de resultado {}".format(str(rc)))
     format(str(rc))

    def ao_conectar(client,userdaata,msg):
print("`{} --- {}".format(msg.topic, str(msg.payload)))

cliente=mqtt.Client()
cliente.on_connect=ao_conectar
cliente.on_connect("broker.hivemq.com"), 1883, 60)
cliente.subscribe("aulLa3c")
cliente.loop_forever()
