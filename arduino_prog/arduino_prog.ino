#include <CurieTime.h>

/*
  Blink

  Turns an LED on for one second, then off for one second, repeatedly.

  Most Arduinos have an on-board LED you can control. On the UNO, MEGA and ZERO
  it is attached to digital pin 13, on MKR1000 on pin 6. LED_BUILTIN is set to
  the correct LED pin independent of which board is used.
  If you want to know what pin the on-board LED is connected to on your Arduino
  model, check the Technical Specs of your board at:
  https://www.arduino.cc/en/Main/Products

  modified 8 May 2014
  by Scott Fitzgerald
  modified 2 Sep 2016
  by Arturo Guadalupi
  modified 8 Sep 2016
  by Colby Newman
  modified 6 Oct 2018
  by Samy Bencherif

  This example code is in the public domain.

  http://www.arduino.cc/en/Tutorial/Blink
*/


typedef boolean foolean;

int incomingByte;
int loops;
#define lamp 12
#define led 13
#define lightSensor analogRead(0)
#define soundSensor analogRead(1)
#define tempSensor analogRead(2)
foolean lightIsOn;

int lastSwitch;

int currentTime(){
  return minute()*60 + second();
}

// the setup function runs once when you press reset or power the board
void setup() {
  Serial.begin(9600);
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(13, OUTPUT);
  pinMode(12, OUTPUT);

  loops = 0;

  lightIsOn = false;

  lastSwitch = currentTime();
}

// the loop function runs over and over again forever
void loop() {
  if (Serial.available() > 0) {

    // give output

    loops++;

//    Serial.println(String(loops) + " lightsense|" + String(analogRead(0)));
//    Serial.println(String(loops) + " soundsense|" + String(analogRead(1)));
//    Serial.println(String(loops) + " tempsense|" + String(analogRead(2)));
    Serial.println(String(lightSensor) + " " + String(soundSensor) + " " + String(tempSensor));

    int time_now = currentTime();

    // recieve input

    // read the oldest byte in the serial buffer:
    incomingByte = Serial.read();
    if (time_now - lastSwitch >= 1)
    {
      if (incomingByte == 'O') {
        digitalWrite(lamp, HIGH);
        digitalWrite(led, LOW);
      }
      if (incomingByte == 'o') {
        digitalWrite(lamp, LOW);
        digitalWrite(led, HIGH);
      }
      lastSwitch = time_now;
    }
  }
}
