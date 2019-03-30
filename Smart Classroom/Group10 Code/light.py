#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21,GPIO.OUT)
# This is the Subscriber

occupied_latency = 5

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("Group10/Seat_Occupancy")

def on_message(client, userdata, msg):

    if msg.payload.decode() == "Occupied":    #data published over Seat_Occupancy topic decoded and compared
        print("Occupied")
        print ("LED on")
        GPIO.output(21,GPIO.HIGH)             #if Occupied led on
        time.sleep(occupied_latency)
        #client.disconnect()
    else:
        print ("LED off")
        GPIO.output(21,GPIO.LOW)             #if not Occupied led off


client = mqtt.Client()              #create client for mqtt server
client.connect("localhost",1883,60) #establish connection

client.on_connect = on_connect      #on_connect and on_message function is called in loop forever
client.on_message = on_message

client.loop_forever()
