 #include <WiFi.h>
#include "AdafruitIO_WiFi.h"
#include <Adafruit_Sensor.h>
#include "DHT.h"
 
#define WIFI_SSID       "Vodafone-D8823A"
#define WIFI_PASS       "8SR7QN66vK"

#define IO_USERNAME  "Barca88"
#define IO_KEY       "aio_KgtP88Z5IAEdT78vSQOfTQ6Zj7xK"

#define DHT11PIN 27 
#define DHT11TYPE DHT11         // DHT 11 


DHT dht11(DHT11PIN, DHT11TYPE);

 
// Connect to Wi-Fi and Adafruit IO handel 
AdafruitIO_WiFi io(IO_USERNAME, IO_KEY, WIFI_SSID, WIFI_PASS);
 
// Create a feed object that allows us to send data to
AdafruitIO_Feed *temperatura = io.feed("Temperature");
AdafruitIO_Feed *humidade = io.feed("Humidity");
AdafruitIO_Feed *heatIndex = io.feed("HeatIndex");

 
void setup() {
  // Enable the serial port so we can see updates
  Serial.begin(9600);
  
  WiFi.softAP(WIFI_SSID, WIFI_PASS);
  
  // Connect to Adafruit IO
  io.connect();
 
  dht11.begin();
  
  while(io.status() < AIO_CONNECTED){
    Serial.print(".");
    delay(500);
  }
}
 
void loop() {

  io.run();

// Read all temperature and humidity sensor data
  float t = dht11.readTemperature();
  float h = dht11.readHumidity();
  float hIndex = dht11.computeHeatIndex(t,h,false);
  
  // check if returns are valid and print the sensor data
  if(isnan(t)){} else {
    temperatura->save(t);
  }
  if(isnan(h)){} else {
    humidade->save(h);
  }
  if(isnan(hIndex)){} else {
    heatIndex->save(hIndex);
  }
  delay(180000);       // print new values every 3 minutes
}
