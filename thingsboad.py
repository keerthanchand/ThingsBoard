import paho.mqtt.client as paho  # mqtt library
import os
import json
import time
import random
from datetime import datetime

ACCESS_TOKEN = '9QgFqcwTsfpe1fYUtnRQ'  # Token of your device
broker = "192.168.0.139"  # host name
port = 1883  # data listening port


def on_publish(client, userdata, result):  # create function for callback
    print("data published to thingsboard \n")
    pass


client1 = paho.Client("control1")  # create client object
client1.on_publish = on_publish  # assign function to callback
client1.username_pw_set(ACCESS_TOKEN)  # access token from thingsboard device
client1.connect(broker, port, keepalive=60)  # establish connection

while True:
    n = random.randint(1,50)
    k = random.randint(1,40)
    payload = "{"
    payload += "\"Humidity\":";
    payload += str(n);
    payload += ",";
    payload += "\"Temperature\":";
    payload += str(k);
    payload += "}"
    ret = client1.publish("v1/devices/me/telemetry", payload)  # topic-v1/devices/me/telemetry
    print("Please check LATEST TELEMETRY field of your device")
    print(payload);
    time.sleep(3)