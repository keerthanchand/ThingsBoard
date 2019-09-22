import paho.mqtt.client as paho  # mqtt library
import time
import serial
from time import sleep
import sys


COM = 'COM5'# /dev/ttyACM0 (Linux)
BAUD = 9600

ser = serial.Serial(COM, BAUD, timeout = .1)

print('Waiting for device');
sleep(3)
print(ser.name)

if("-m" in sys.argv or "--monitor" in sys.argv):
	monitor = True
else:
	monitor= False


ACCESS_TOKEN = '716SEv2C5uBPxuYlfoVz'  # Token of your device
broker = "demo.thingsboard.io"  # host name
port = 1883  # data listening port


def on_publish(client, userdata, result):  # create function for callback
    print("data published to thingsboard \n")
    pass


client1 = paho.Client("control1")  # create client object
client1.on_publish = on_publish  # assign function to callback
client1.username_pw_set(ACCESS_TOKEN)  # access token from thingsboard device
client1.connect(broker, port, keepalive=60)  # establish connection

while True:
    val = str(ser.readline().decode().strip('\r\n'))
    k = val
    payload = "{"
    payload += "\"Temperature\":";
    payload += str(k);
    payload += "}"
    ret = client1.publish("v1/devices/me/telemetry", payload)  # topic-v1/devices/me/telemetry
    print("Please check LATEST TELEMETRY field of your device")
    print(payload);
    time.sleep(1)