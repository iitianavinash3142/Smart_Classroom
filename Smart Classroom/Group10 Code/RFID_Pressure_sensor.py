#!/usr/bin/env python

#Libraries
import RPi.GPIO as GPIO
import SimpleMFRC522
import datetime
import json
import paho.mqtt.client as mqtt
import serial
import RPi.GPIO as GPIO
import time


class_time = 60  # full class time in seconds
data_read_lapse = 1  # lapse given in seconds to read data
pressure_sensor_counter = 0 #counter for the number of times seat occupancy status os 1
curr_time = datetime.datetime.now()  #start time

ser=serial.Serial("/dev/ttyACM0",9600)  #change ACM number as found from ls /dev/tty/ACM*
ser.baudrate=9600

reader = SimpleMFRC522.SimpleMFRC522()
data = {"rfid":[],"proxies":[] ,"present":[],"exit_in_midclass":[]} #this dictionary stores all the attendence related data
c=0 #counter for reading count
try:
    while curr_time + datetime.timedelta(seconds = class_time) > datetime.datetime.now():

        id, text = reader.read() #read RFID tag
        id = str(id)
        if id != "None":    #if RFID reader read Tag then append in dictionary and increament counter
            c=c+1
            data["rfid"].append(id)

        try:
            read_ser=ser.readline()             #reads pressure sensor data from aurdino
            read_ser = int(read_ser)
            # time.sleep(1)
            pressure_sensor_counter += read_ser
            print(read_ser)
        except ValueError:
            pass
        # print(data)
        time.sleep(data_read_lapse)            #time lapse of 1 second in reading

finally:
    GPIO.cleanup()

client = mqtt.Client()               #create client for mqtt server
client.connect("localhost",1883,60)  #establish connection


data["rfid"].sort()
unique_id = list(set(data["rfid"]))   #unique id equals list of unique id tag read from reader
unique_id_count = len(unique_id)       #respective count
rfid_counter = len(data["rfid"])      #RFID counter equals count of data read


#student present
if unique_id_count == 1 and rfid_counter == c and pressure_sensor_counter >= c-10:
    data["present"].append(unique_id[0])
    client.publish("Group10/attendence", json.dumps({"idx":["present", str(unique_id[0])]}))  #data of present student published in attendence topic

#student exit in mid class
elif unique_id_count == 1 and pressure_sensor_counter > 0 and rfid_counter > 0 :
    data["exit_in_midclass"].extend(list(unique_id))
    for i in unique_id:
        client.publish("Group10/attendence", json.dumps({"idx":["exit_mid", str(i)]}))  #data of students tried to exit in mid class published in attendence topic

#students involved in proxies plus exit in mid class
elif unique_id_count > 1 and pressure_sensor_counter > 0 and rfid_counter > 0 :
    data["proxies"].extend(list(unique_id))
    print(unique_id)
    for i in unique_id:
        client.publish("Group10/attendence", json.dumps({"idx":["proxy", str(i)]}))   #data of students involved in proxy published in attendence topic
    data["exit_in_midclass"].extend(list(unique_id))
    for i in unique_id:
        client.publish("Group10/attendence", json.dumps({"idx":["exit_mid", str(i)]}))  #data of students tried to exit in mid class published in attendence topic

#students involved in proxies
elif unique_id_count >= 1:
    data["proxies"].extend(list(unique_id))
    for i in unique_id:
        client.publish("Group10/attendence", json.dumps({"idx":["proxy", str(i)]}))     #data of students involved in proxy published in attendence topic
else :
    pass

client.disconnect()    #client disconnect

data["count"] = c
with open('data.json', 'w') as outfile:  #all data dumped in json file
    json.dump(data, outfile)
