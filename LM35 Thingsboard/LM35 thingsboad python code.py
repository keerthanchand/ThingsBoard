import paho.mqtt.client as paho  
import time
import serial
from time import sleep
import sys


COM = 'COM5'
BAUD = 9600

ser = serial.Serial(COM, BAUD, timeout = .1)

print('Waiting for device');
sleep(3)
print(ser.name)

if("-m" in sys.argv or "--monitor" in sys.argv):
	monitor = True
else:
	monitor= False


ACCESS_TOKEN = 'xxxxxxxxxxxxxxxx'  
broker = "demo.thingsboard.io" 
port = 1883 


def on_publish(client, userdata, result): 
    print("data published to thingsboard \n")
    pass


client1 = paho.Client("control1")  
client1.on_publish = on_publish  
client1.username_pw_set(ACCESS_TOKEN) 
client1.connect(broker, port, keepalive=60) 

while True:
    val = str(ser.readline().decode().strip('\r\n'))
    k = val
    payload = "{"
    payload += "\"Temperature\":";
    payload += str(k);
    payload += "}"
    ret = client1.publish("v1/devices/me/telemetry", payload)  
    print("Please check LATEST TELEMETRY field of your device")
    print(payload);
    time.sleep(1)
