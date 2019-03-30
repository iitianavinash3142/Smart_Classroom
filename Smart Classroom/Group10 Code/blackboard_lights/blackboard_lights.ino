#include <CapacitiveSensor.h>

/*
 * Uses a high value resistor e.g. 10 megohm between send pin and receive pin
 * Resistor effects sensitivity, experiment with values, 50 kilohm - 50 megohm. Larger resistor values yield larger sensor values.
 * Receive pin is the sensor pin - try different amounts of foil/metal on this pin
 * Best results are obtained if sensor foil and wire is covered with an insulator such as paper or plastic sheet
 */


CapacitiveSensor   cs_1_3 = CapacitiveSensor(11,3);        

void setup()                    
{

   cs_1_3.set_CS_AutocaL_Millis(0xFFFFFFFF);     // turn off autocalibrate on channel 1 - just as an example
   Serial.begin(9600);

}

void loop()                    
{
    int start = millis();
    int total1 =  cs_1_3.capacitiveSensor(30);

    int threshold = 10000;
    Serial.println(total1);
    delay(300);
    
}
