#!/usr/bin/env python3

#Libraries
import paho.mqtt.client as mqtt
import time
import json
mp={}  #mp dictionary stores data of class
mp["413792445030"] = "Student1"
mp["231356239888"] = "Student2"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("Group10/attendence")       #suscribe to attendence topic from where data need to be recieved

def on_message(client, userdata, msg):
    payload  = json.loads(msg.payload.decode())
    print(payload)
    with open('attendence_sheet.json') as fh:   #payload will contain whether student x is present,absent,proxy etc
        a = json.load(fh)                       #this data is dumped in the attendence sheet
        a[mp[payload["idx"][1]]] = payload["idx"][0]
        with open('attendence_sheet.json', 'w') as fh:  #attedence sheet contains the attendence record of the classroom
            json.dump(a, fh)


client = mqtt.Client()              #create client for mqtt server
client.connect("localhost",1883,60) #establish connection

client.on_connect = on_connect      #on_connect and on_message function is called in loop forever
client.on_message = on_message

client.loop_forever()
