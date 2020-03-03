import paho.mqtt.client as paho
import os
import json
import time
import random
from datetime import datetime

ACCESS_TOKEN = 'access_token_here'
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
    n = random.randint(1,50)
    k = random.randint(1,40)
    payload = "{"
    payload += "\"Humidity\":";
    payload += str(n);
    payload += ",";
    payload += "\"Temperature\":";
    payload += str(k);
    payload += "}"
    ret = client1.publish("v1/devices/me/telemetry", payload)
    print("Please check LATEST TELEMETRY field of your device")
    print(payload);
    time.sleep(3)
