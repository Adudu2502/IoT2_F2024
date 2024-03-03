import paho.mqtt.subscribe as subscribe
print("Subxcribe MQTT script running!")

def on_message_print(client, userdata, message):
    print("%s %s" % (message.topic, message.payload))
    

subscribe.callback(on_message_print, "paho/test/topic", hostname="20.234.68.196", userdata={"message_count": 0})