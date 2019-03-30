Group 10
Smart Classroom

Members:
		abhishek kumar kotiya 160101007
		avinash uchchainiya 160101018
		rajas bhadke 160101021
		durgesh yadav 160101027


Sensor used : RFID reader and RFID-card, Capacitive-Resistance , Temperature sensor , Raspberry pi wifi adapter, Digital Light Sensor, DC motor

Features :

1 )  Attendence and Proxy Detection :
 	 We are using RFID for unique identification on the basis of id cards . To check whether the student is present for the entire class duration we are using capacitive sensor to detect if a student is sitting .
 	 IMPLEMENTATION : 
 					The script RFID_Pressure_sensor.py will collect RFID and Pressure sensor data at regular intervals , after a fixed interval of time if data is vlaid then its attendence will be marked as present and its data will be uploaded in MQTT server, the data which will be uploaded by RFID_Pressure_sensor.py script will be collected by Attendence subscription.py script.

2 )  Seat Occupancy Status :
	 Using the capacitive sensor we will display the seat occupancy status and display which seats are occupied .


3 )  Automatic Light and Fan :
	 From the seat occupancy status we can turn on the light and fan in the proximity of that seat if it is occupied or turn off if it not occupied .
	 IMPLEMENTATION : 
					Using Pressure_sensor_data.py script will continuously publish the occupancy status of the seat to the MQTT server, the light of the occupied seat will be turned on and off by the script light.py , the fan would be turned on and off on the basis of the occupied seat and the value of the temperature sensor. 

4 )  Mid Class Entry Exit Detection :
	 We will detect and alert the professor if any student is trying to exit mid class using seat occupancy data. 

 
5 )  Control Blackboard Lights :
	 we are using multiple capacitive sensors to detect motion around the board and turn on the lights if professor is near the blackboard .


Python Scripts :

1 . RFID_Pressure_sensor.py : 
								This script continuously collects RFID and pressure sensor data for a fixed time interval, validates the data and publishes the attendence status 									of students.
2 . attendence_subscription.py :
								This script maintains a database of the attendence of the classroom on the basis of the the data collected by the RFID_Pressure_sensor.

3 . pressure_sensor_data.py : 
								This script continuously collects and publishes the seat occupancy status on the MQTT server.
4 . light.py :
								This script turns ON the light corresponding to the occupied seat.

5 . capacitive_sensor.ino   :  					arduino file for  calculating the capacitive sensor data .

5 . blackboard_lights.ino   :  					arduino file for  blackboard light control .

6.  Automatic_Fan_Light_control.ino   :                         arduino file for fan control using temperatute sensor

Steps to Execute :

1 ) Connect the RFID sensor to Raspberry pi .
2 ) Connect the Capacitive Sensor to Arduino .
3 ) Upload the capacitive sensor code (capacitive_sensor.ino) to Arduino .
4 ) Connect the Arduino and wifi-Adapter to Raspberry pi .
5 ) For attendence in classroom ,  simultaneously run the scripts RFID_Pressure_sensor.py and Attendence_subscription.py .
6 ) For automated light contro1 run scripts Pressure_sensor_data.py and Light.py simultaneously , if the seat is occupied the light will turn on .
7 ) For blackboard light control , run the blackboard_lights.ino code in arduino. 
