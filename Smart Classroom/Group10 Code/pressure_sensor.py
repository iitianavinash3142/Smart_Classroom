import serial
import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt

ser=serial.Serial("/dev/ttyACM0",9600)  #change ACM number as found from ls /dev/tty/ACM*
ser.baudrate=9600

while True:
    read_ser=ser.readline()    #reads data from aurdino

    try:
        read_ser = int(read_ser)
    except:
	    time.sleep(1)
	    try:
	           read_ser = int(read_ser)
	    except:
    	       print ("This is an error message!")

    client = mqtt.Client()                   #create client for mqtt server
    client.connect("localhost",1883,60)      #establish connection
    if read_ser == 1:
        client.publish("Group10/Seat_Occupancy", "Occupied") #publish data to Seat Occupancy topic if seat Occupied
        client.disconnect() #client disconnect
        print(read_ser)
    else:
        client.publish("Group10/Seat_Occupancy", "Empty")   #publish data to Seat Occupancy topic if seat not Occupied
        client.disconnect()  #client disconnect
        print(read_ser)
