#include <Wire.h>                     // Libraries for Digital Light Sensor
#include <Digital_Light_TSL2561.h>

#include "DHT.h"     // Including library for dht

// ** Light Pins **
#define Light_Pin 10

// ** Fan Pins **
#define Fan_Pin 6


//** Tempreture Sensor Pins **
#define DHTPIN 12 
#define DHTTYPE DHT11   // DHT 11

DHT dht(DHTPIN, DHTTYPE);

void setup() {
    Wire.begin();                   // Setup For see Seriel monitor
    Serial.begin(9600);
      
     
    Serial.println("DHTxx test!");   // Setup for Temperature sensor
    dht.begin();    
    
    pinMode(Fan_Pin,OUTPUT);         // Pin Mode for Fan      
    

    TSL2561.init();                  // Setup For Digital Light Sensor

    pinMode(Light_Pin,OUTPUT);       // Pin Mode For Light
}

void loop() {
                           
   unsigned int temp = dht.readTemperature();  // store Tempreture value
   
   Serial.print("Temperature: ");   // Print In Serial Monitor  
   Serial.print(temp);
   Serial.println(" *C");

   // ** Conditions For Fan Control According to Class Room Temperature 
   
   if(temp < 25){
    FanOff();
   }
   else if(temp >= 25 && temp <= 30 ){
    FanOn_with_one_third_speed();
   }
  else if(temp > 30 && temp <= 35){
    FanOn_with_two_third_speed();
   }
  else if(temp > 35){
    FanOn(); 
   }else;

  // **** Automatic Light ON of Class ROOM ****

  Serial.print("The Light value is: ");
  Serial.println(TSL2561.readVisibleLux());
  
  unsigned int Light = TSL2561.readVisibleLux();    // Store digital light sensor
  
  if(Light < 100){
    LightOn();
  }
  else{
    LightOff();   
  }

}
 
void LightOn(){               // Function for Light On
  digitalWrite(Light_Pin,HIGH);
}

void LightOff(){             // Function for Light OFF
  digitalWrite(Light_Pin,LOW);
}

void FanOff(){               // Function for Fan OFF
  digitalWrite(Fan_Pin,LOW);
 }

void FanOn(){                 // Function for Fan On
  digitalWrite(Fan_Pin,HIGH);
 }

void FanOn_with_one_third_speed(){   // Function for Fan speed one third of total speed
  digitalWrite(Fan_Pin,HIGH);
  delay(50);
  digitalWrite(Fan_Pin,LOW);
  delay(100);
}

void FanOn_with_two_third_speed(){   // Function for Fan speed Two third of total speed
  digitalWrite(Fan_Pin,HIGH);
  delay(100);
  digitalWrite(Fan_Pin,LOW);
  delay(50);
}
