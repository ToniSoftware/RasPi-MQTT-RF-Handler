# RasPi-MQTT-RF-Handler

A Python script written for an Raspberry Pi

What is this python script for?
- You'll establish an connection with or without ssl to an MQTT-Broker
- Subscribe to topics
- Interact with payloads published in the topic
- Control  RF Switches with raspberry-remote (https://github.com/xkonni/raspberry-remote)
- Send a status message on a status topic

Here you get some example code to add a Raspberry Pi to Home Assistant (https://www.home-assistant.io/)

'''
light:
  - platform: mqtt
    name: "LEDs"
    state_topic: "room/leds/switch/status"
    command_topic: "room/leds/switch"
    qos: 0
    payload_on: "ON"
    payload_off: "OFF"
    optimistic: false
    retain: true
'''