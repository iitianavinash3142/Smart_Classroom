#include <CapacitiveSensor.h>

/*
 * Uses a high value resistor e.g. 10 megohm between send pin and receive pin
 * Resistor effects sensitivity, experiment with values, 50 kilohm - 50 megohm. Larger resistor values yield larger sensor values.
 * Receive pin is the sensor pin - try different amounts of foil/metal on this pin
 * Best results are obtained if sensor foil and wire is covered with an insulator such as paper or plastic sheet
 */


CapacitiveSensor   cs_2_4 = CapacitiveSensor(2,4);        // 10 megohm resistor between pins 4 & 2, pin 2 is sensor pin, add wire, foil 4 is wire 2 is resistor
CapacitiveSensor   cs_2_6 = CapacitiveSensor(2,6);        // 10 megohm resistor between pins 4 & 6, pin 6 is sensor pin, add wire, foil
CapacitiveSensor   cs_2_8 = CapacitiveSensor(2,8);        // 10 megohm resistor between pins 4 & 8, pin 8 is sensor pin, add wire, foil

void setup()                    
{

   cs_2_4.set_CS_AutocaL_Millis(0xFFFFFFFF);     // turn off autocalibrate on channel 1 - just as an example
   Serial.begin(9600);

}

void loop()                    
{
    int start = millis();
    int total1 =  cs_2_4.capacitiveSensor(30);
    int total2 =  cs_2_6.capacitiveSensor(30);
    int total3 =  cs_2_8.capacitiveSensor(30);

//    /Serial.print(millis() - start);        // check on performance in milliseconds
//    Serial.print("\t");                    // tab character for debug window spacing

//    Serial.print(total1);                  // print sensor output 1
//    Serial.print("\t");
//    Serial.print(total1); 
//    Serial.print("\t");// print sensor output 2
//    Serial.println(total3);  
//    Serial.print("\t");
//    Serial.println(total3);                // print sensor output 3

    delay(10);                             // arbitrary delay to limit data to serial port 

    long threshold = 1000;
    int to_send = 1;
    if (total1 > threshold || total3 > threshold ) ; // if all sensor data greater than threshold implies seat occupied
    else to_send = 0;

    Serial.println(to_send);    // sent data serially to raspberry pi
    
}
