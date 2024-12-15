#include <Wire.h> // Include the Wire library for I2C communication
#include <Adafruit_MotorShield.h> // Include the Adafruit Motor Shield library
#include <Adafruit_NeoPixel.h> // Include the Adafruit NeoPixel library

// Create the motor shield object
Adafruit_MotorShield AFMS = Adafruit_MotorShield(); 

// Connect stepper motors to the motor shield
Adafruit_StepperMotor *stepper1 = AFMS.getStepper(516, 1); // Stepper 1 on M1 and M2
Adafruit_StepperMotor *stepper2 = AFMS.getStepper(516, 2); // Stepper 2 on M3 and M4

// NeoPixel setup
#define LED_PIN 12 // Pin for NeoPixel LEDs
#define LED_COUNT 100 // Number of NeoPixel LEDs

Adafruit_NeoPixel strip(LED_COUNT, LED_PIN, NEO_GRB + NEO_KHZ800); // NeoPixel configuration

// Configurable delay times
int greenDelay = 50; // Delay for turning LEDs green (in ms)
int blueFlashInterval = 600; // Flash interval for blue LEDs (in ms)

// Additional motor setup
const int dirPin1 = 8; // Direction pin for first motor
const int stepPin1 = 9; // Step pin for first motor
const int dirPin2 = 10; // Direction pin for second motor
const int stepPin2 = 11; // Step pin for second motor

// External stepper motor pins
const int dirPin3 = 0;
const int stepPin3 = 1;
const int dirPin4 = 2;
const int stepPin4 = 3;
const int dirPin5 = 4;
const int stepPin5 = 5;
const int dirPin6 = 6;
const int stepPin6 = 7;

// Stepper motor settings
const int stepsPerRevolution = 516; // Steps for one full revolution
const int rpm = 10; // Speed in RPM
const long delayPerStep = (60L * 1000L * 1000L) / (stepsPerRevolution * rpm); // Delay per step (in microseconds)

// Sensor setup
int Right_Sensor = A0; // Analog pin for the sensor
int Right_Sensor_Read; // Variable to store sensor readings

void setup() {
  Serial.begin(9600); // Start serial communication
  AFMS.begin(); // Initialize the motor shield
  strip.begin(); // Initialize NeoPixel object
  strip.setBrightness(10); // Set LED brightness
  strip.clear(); // Turn off all LEDs
  strip.show();
  setDefaultWhite();

  // Configure pins for external stepper motors
  pinMode(stepPin1, OUTPUT);
  pinMode(dirPin1, OUTPUT);
  pinMode(stepPin2, OUTPUT);
  pinMode(dirPin2, OUTPUT);
  pinMode(stepPin3, OUTPUT);
  pinMode(dirPin3, OUTPUT);
  pinMode(stepPin4, OUTPUT);
  pinMode(dirPin4, OUTPUT);
  pinMode(stepPin5, OUTPUT);
  pinMode(dirPin5, OUTPUT);
  pinMode(stepPin6, OUTPUT);
  pinMode(dirPin6, OUTPUT);

  // Sensor pin configuration
  pinMode(Right_Sensor, INPUT);
}

void setDefaultWhite() {
  strip.fill(strip.Color(255, 255, 255)); // Set white color
  strip.show();
}

// Function to turn LEDs green in sequence
void turnGreen() {
  for (int i = 0; i < LED_COUNT; i++) {
    strip.setPixelColor(i, 0, 255, 0); // Set green color
    strip.show();
    delay(greenDelay);
  }
}

// Function to flash all LEDs blue
void flashBlue() {
  strip.fill(strip.Color(0, 0, 255)); // Set blue color
  strip.show();
  delay(blueFlashInterval);
  strip.clear(); // Turn off LEDs
  strip.show();
  delay(blueFlashInterval);
  setDefaultWhite();
}

// Function to rotate an external stepper motor clockwise
void rotateExternalStepper(int dirPin, int stepPin) {
  digitalWrite(dirPin, LOW); // Set direction to clockwise
  for (int i = 0; i < stepsPerRevolution; i++) {
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(delayPerStep / 2);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(delayPerStep / 2);
  }
}

// Function to rotate an external stepper motor counterclockwise
void rotateExternalStepper2(int dirPin, int stepPin) {
  digitalWrite(dirPin, HIGH); // Set direction to counterclockwise
  for (int i = 0; i < stepsPerRevolution; i++) {
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(delayPerStep / 2);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(delayPerStep / 2);
  }
}

void loop() {
  int sensorValue = analogRead(A0); // Read sensor value
  Serial.println(sensorValue); // Print sensor value to Serial Monitor
  delay(100);

  // Check if data is available from Serial
  if (Serial.available() > 0) {
    int receivedNumber = Serial.parseInt(); // Parse received data

    // Perform actions based on received number
    if (receivedNumber == 1) {
      turnGreen();
      rotateExternalStepper(dirPin1, stepPin1);
      digitalWrite(stepPin1, LOW);
      digitalWrite(dirPin1, LOW);
      unsigned long startTime = millis();
      while (millis() - startTime < 2000) {
        flashBlue();
      }
    } else if (receivedNumber == 2) {
      turnGreen();
      rotateExternalStepper(dirPin2, stepPin2);
      digitalWrite(stepPin2, LOW);
      digitalWrite(dirPin2, LOW);
      unsigned long startTime = millis();
      while (millis() - startTime < 2000) {
        flashBlue();
      }
    } else if (receivedNumber == 3) {
      turnGreen();
      rotateExternalStepper(dirPin3, stepPin3);
      digitalWrite(stepPin3, LOW);
      digitalWrite(dirPin3, LOW);
      unsigned long startTime = millis();
      while (millis() - startTime < 2000) {
        flashBlue();
      }
    } else if (receivedNumber == 4) {
      turnGreen();
      rotateExternalStepper(dirPin4, stepPin4);
      digitalWrite(stepPin4, LOW);
      digitalWrite(dirPin4, LOW);
      unsigned long startTime = millis();
      while (millis() - startTime < 2000) {
        flashBlue();
      }
    } else if (receivedNumber == 5) {
      turnGreen();
      rotateExternalStepper2(dirPin5, stepPin5);
      digitalWrite(stepPin5, LOW);
      digitalWrite(dirPin5, LOW);
      unsigned long startTime = millis();
      while (millis() - startTime < 2000) {
        flashBlue();
      }
    } else if (receivedNumber == 6) {
      turnGreen();
      rotateExternalStepper(dirPin6, stepPin6);
      digitalWrite(stepPin6, LOW);
      digitalWrite(dirPin6, LOW);
      unsigned long startTime = millis();
      while (millis() - startTime < 2000) {
        flashBlue();
      }
    }
    delay(50); // Delay before next loop iteration
  }
}
