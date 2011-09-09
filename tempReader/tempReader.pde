#include "DHT22.h"

// Connect a 4.7K resistor between VCC and the data pin (strong pullup)
#define DHT22_PIN 12

// Setup a DHT22 instance
DHT22 myDHT22(DHT22_PIN);

char msg = ' ';	// for incoming serial data

void setup(void)
{
  // start serial port
  Serial.begin(9600);
}

void loop(void)
{ 
  DHT22_ERROR_t errorCode;

  if (Serial.available() > 0) {
    msg = Serial.read();
    if (msg == 'r') {
      //Serial.print("Requesting data...");
      errorCode = myDHT22.readData();
      switch(errorCode)
      {
        case DHT_ERROR_NONE:
          //Serial.print("Got Data ");
          Serial.print(myDHT22.getTemperatureF());
          //Serial.print("F ");
          Serial.print(" ");
          Serial.print(myDHT22.getHumidity());
          //Serial.println("%");
          break;
        case DHT_ERROR_CHECKSUM:
          Serial.print("check sum error ");
          Serial.print(myDHT22.getTemperatureF());
          Serial.print("F ");
          Serial.print(myDHT22.getHumidity());
          Serial.println("%");
          break;
        case DHT_BUS_HUNG:
          Serial.println("BUS Hung ");
          break;
        case DHT_ERROR_NOT_PRESENT:
          Serial.println("Not Present ");
          break;
        case DHT_ERROR_ACK_TOO_LONG:
          Serial.println("ACK time out ");
          break;
        case DHT_ERROR_SYNC_TIMEOUT:
          Serial.println("Sync Timeout ");
          break;
        case DHT_ERROR_DATA_TIMEOUT:
          Serial.println("Data Timeout ");
          break;
        case DHT_ERROR_TOOQUICK:
          Serial.println("Polled too quick ");
          break;
      }
    }
  }
}
