import paho.mqtt.subscribe as subscribe
from gpiozero import LED
from time import sleep

red = LED(17)

print("Subxcribe MQTT script running!")

def on_message_print(client, userdata, message):
    print("%s %s" % (message.topic, message.payload))
    status = message.payload.decode() 

    if status == "taend":
        red.on()
    if status == "sluk":
        red.offf()
subscribe.callback(on_message_print, "LED", hostname="20.234.68.196", userdata={"message_count": 0})