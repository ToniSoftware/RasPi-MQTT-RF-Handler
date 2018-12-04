#!/usr/bin/env python
import socket
import time
import subprocess
import ssl
import paho.mqtt.client as mqtt

# We're setting the codes we need to control the switches-> look up how the codes should look like in raspberry-remote docu
code_dict = {    "room/leds/switch":     {"ON": "11111 1 1", "OFF": "11111 1 0"},
                "room/ikealamp/switch":    {"ON": "11111 2 1", "OFF": "11111 2 0"},
                "room/table/lamp/switch":    {"ON": "11111 3 1", "OFF": "11111 3 0"},
            }

# On connect we're subscribing to topic "room/#"
def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("room/#")

# On message we're definig our handler for an message we expect
def on_message(client, userdata, msg):
  topic = str(msg.topic)
  payload = msg.payload.decode(encoding='UTF-8')
  print("received message in " + topic + ": " + payload)
  send_code(topic, payload)

# What we're doing when we get a message in an subscribed topic
def send_code(topic, payload):
  if payload == "ON" or payload == "OFF":
      try:
          subprocess.Popen("sudo /home/lights/raspberry-remote/send " + code_dict[topic][payload], shell = True)
          print("turning switch: " + topic)
          client.publish(topic + "/status", payload)
          print("published: " + payload)
      except KeyError:
          pass

# Establishing connection
client = mqtt.Client("pi")
client.username_pw_set("username", "password")
# Comment this line if you don't use SSL for the connection to your MQTT-Broker
client.tls_set(ca_certs=None, certfile=None, keyfile=None, cert_reqs=ssl.CERT_REQUIRED,ciphers=None)
# If you don't use SSL, change 8883 to 1883
client.connect("hostname",8883,60)

# Waiting for action
client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()