 #include <ESP8266WiFi.h>
#include "AdafruitIO_WiFi.h"
#include "DHT.h"
 
#define WIFI_SSID       "Vodafone-D8823A"
#define WIFI_PASS       "8SR7QN66vK"

#define IO_USERNAME  "Barca88"
#define IO_KEY       "aio_KgtP88Z5IAEdT78vSQOfTQ6Zj7xK"
//#define IO_USERNAME    "addams81"
//#define IO_KEY         "aio_QSXe69WpRd5KuLgycMuGsXWa2zTT"

#define AD A0
#define DO 5

// Connect to Wi-Fi and Adafruit IO handel 
AdafruitIO_WiFi io(IO_USERNAME, IO_KEY, WIFI_SSID, WIFI_PASS);
 
// Create a feed object that allows us to send data to

AdafruitIO_Feed *somAnalog = io.feed("Workshop somAnalog");
AdafruitIO_Feed *somDigital = io.feed("Workshop somDigital");
 
void setup() {
  // Enable the serial port so we can see updates
  Serial.begin(9600);
 
  // Connect to Adafruit IO
  io.connect();
 
  int last = 0;
  int value = 0;
  // configure input to interrupt
  // pinMode(AD, INPUT);
}
 
void loop() {
  float value;
  float som;
  io.run();
  
  value = digitalRead(DO);
  som = analogRead(AD);
  if(som < 753 || som > 760){
     somAnalog->save(som);
     
     somDigital->save(value);
  }
  
  delay(1000);       // print new values every 10 seconds
}
