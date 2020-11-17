#include <ESP8266WiFi.h>
#include "AdafruitIO_WiFi.h"
#include "DHT.h"

#define WIFI_SSID       "Vodafone-D8823A"
#define WIFI_PASS       "8SR7QN66vK"

#define IO_USERNAME    "addams81"
#define IO_KEY         "aio_QSXe69WpRd5KuLgycMuGsXWa2zTT"

#define DHT11PIN 0        // define the digital I/O pin


#define DHT11TYPE DHT11         // DHT 11 


DHT dht11(DHT11PIN, DHT11TYPE);


// Connect to Wi-Fi and Adafruit IO handel 
AdafruitIO_WiFi io(IO_USERNAME, IO_KEY, WIFI_SSID, WIFI_PASS);

// Create a feed object that allows us to send data to
AdafruitIO_Feed *temperatura = io.feed("Workshop temperature");

AdafruitIO_Feed *humidade = io.feed("Workshop humidity");


AdafruitIO_Feed *somAnalog = io.feed("Workshop somAnalog");

AdafruitIO_Feed *somDigital = io.feed("Workshop somDigital");


void setup() {
  // Enable the serial port so we can see updates
  Serial.begin(9600);

  // Connect to Adafruit IO
  io.connect();

  dht11.begin();
  while(io.status() < AIO_CONNECTED) 
  {
    Serial.print(".");
    delay(500);
  }
}

void loop() {
  io.run();


// Read all temperature and humidity sensor data
  float t11 = dht11.readTemperature();
  float d11 = dht11.readHumidity();

  // check if returns are valid and print the sensor data
  if (isnan(t11)) {}
  else {
    temperatura->save(t11);
  } 
  if (isnan(d11)) {}
  else {
    humidade->save(d11);
  }

  delay(10000);       // print new values every 10 seconds
}
