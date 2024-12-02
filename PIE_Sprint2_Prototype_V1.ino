#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include <Adafruit_NeoPixel.h>
#include "utility/Adafruit_MS_PWMServoDriver.h"

// Create the motor shield object
Adafruit_MotorShield AFMS = Adafruit_MotorShield(); 

// Connect to a stepper motor (516 steps per revolution) on port M1 and M2
Adafruit_StepperMotor *stepper1 = AFMS.getStepper(516, 1); // Port 1 (M1 and M2)
Adafruit_StepperMotor *stepper2 = AFMS.getStepper(516, 2); // Port 2 (M3 and M4)

// NeoPixel setup
#define LED_PIN 9
#define LED_COUNT 100

Adafruit_NeoPixel strip(LED_COUNT, LED_PIN, NEO_GRB + NEO_KHZ800);

// Configurable delay times
int greenDelay = 50;         // Delay for turning LEDs green (0.05 seconds in ms)
int blueFlashInterval = 600; // Flash interval in milliseconds for blue LEDs

// Additional motor setup
const int dirPin = 0;     // Direction pin
const int stepPin = 1;    // Step pin
const int dirPin2 = 2;    // Direction pin
const int stepPin2 = 3;   // Step pin
const int dirPin3 = 4;    // Direction pin
const int stepPin3 = 5;   // Step pin
const int dirPin4 = 6;    // Direction pin
const int stepPin4 = 7;   // Step pin
const int stepsPerRevolution = 516; // Number of steps for one full revolution
const int rpm = 10;       // Speed in RPM
const long delayPerStep = (60L * 1000L * 1000L) / (stepsPerRevolution * rpm); // Microsecond delay for 10 RPM

// Sensor setup
int Right_Sensor = A0;  // Define the sensor pin
int Right_Sensor_Read;  // Variable to store the sensor reading

void setup() {
  Serial.begin(9600);           // Start serial communication
  AFMS.begin();                 // Initialize the motor shield
  strip.begin();                // Initialize NeoPixel object
  strip.setBrightness(10);      // Set brightness
  strip.clear();                // Ensure LEDs start off
  strip.show();

  pinMode(stepPin, OUTPUT);     // Set step pin as output
  pinMode(dirPin, OUTPUT); 
  pinMode(stepPin2, OUTPUT);    // Set step pin as output
  pinMode(dirPin2, OUTPUT);     // Set direction pin as output
  pinMode(stepPin3, OUTPUT);    // Set step pin as output
  pinMode(dirPin3, OUTPUT); 
  pinMode(stepPin4, OUTPUT);    // Set step pin as output
  pinMode(dirPin4, OUTPUT);     // Set direction pin as output

  // Sensor setup
  pinMode(Right_Sensor, INPUT); // Set the sensor pin as an input
}

void turnGreen() {
  for (int i = 0; i < LED_COUNT; i++) {
    strip.setPixelColor(i, 0, 255, 0); // Green color
    strip.show();
    delay(greenDelay);
  }
}

void flashBlue() {
  strip.fill(strip.Color(0, 0, 255)); // Blue color
  strip.show();
  delay(blueFlashInterval);
  strip.clear(); // Turn off LEDs
  strip.show();
  delay(blueFlashInterval);
}

void rotateStepper(Adafruit_StepperMotor *stepper) {
  stepper->setSpeed(10);                // Set speed to 10 RPM
  stepper->step(516, BACKWARD, SINGLE); // One full rotation backward
}

void rotateExternalStepper(int dirPin, int stepPin) {
  digitalWrite(dirPin, LOW); // Set the direction to clockwise
  for (int i = 0; i < stepsPerRevolution; i++) {
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(delayPerStep / 2);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(delayPerStep / 2);
  }
}

void loop() {
  // Read the sensor value
  Right_Sensor_Read = analogRead(Right_Sensor);
  Serial.println(Right_Sensor_Read); // Print the sensor reading

  // Check for serial input to control motors and LEDs
  if (Serial.available() > 0) {
    int receivedNumber = Serial.parseInt();

    if (receivedNumber == 1) {
      Serial.println("Received 1 from Python!");
      turnGreen();
      rotateStepper(stepper1);
      unsigned long startTime = millis();
      while (millis() - startTime < 2000) {
        flashBlue();
      }
    } else if (receivedNumber == 2) {
      Serial.println("Received 2 from Python!");
      turnGreen();
      rotateStepper(stepper2);
      unsigned long startTime = millis();
      while (millis() - startTime < 2000) {
        flashBlue();
      }
    }
    // Additional cases for other motors
    // ...
    else {
      Serial.println("Invalid input. No motor found.");
    }
  }

  delay(100); // Slight delay for sensor reading and serial handling
}
