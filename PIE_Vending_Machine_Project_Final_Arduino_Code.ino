#include <Wire.h> // Include the Wire library for I2C communication
#include <Adafruit_MotorShield.h> // Include the Adafruit Motor Shield library
#include <Adafruit_NeoPixel.h> // Include the Adafruit NeoPixel library

// Create the motor shield object
Adafruit_MotorShield AFMS = Adafruit_MotorShield(); 

// Connect stepper motors to the motor shield
Adafruit_StepperMotor *stepper1 = AFMS.getStepper(516, 1); // Stepper motor 1 connected to M1 and M2
Adafruit_StepperMotor *stepper2 = AFMS.getStepper(516, 2); // Stepper motor 2 connected to M3 and M4

// NeoPixel setup
#define LED_PIN 12      // Pin connected to NeoPixel LEDs
#define LED_COUNT 100   // Total number of NeoPixel LEDs
Adafruit_NeoPixel strip(LED_COUNT, LED_PIN, NEO_GRB + NEO_KHZ800); // NeoPixel strip configuration

// Configurable delay times
int greenDelay = 50;           // Delay (in ms) for turning LEDs green in sequence
int blueFlashInterval = 600;   // Interval (in ms) for flashing blue LEDs

// External stepper motor setup
const int dirPin1 = 8;  // Direction pin for first external stepper motor
const int stepPin1 = 9; // Step pin for first external stepper motor
const int dirPin2 = 10; // Direction pin for second external stepper motor
const int stepPin2 = 11; // Step pin for second external stepper motor

// Additional external stepper motor pins
const int dirPin3 = 0;  // Direction pin for stepper 3
const int stepPin3 = 1; // Step pin for stepper 3
const int dirPin4 = 2;  // Direction pin for stepper 4
const int stepPin4 = 3; // Step pin for stepper 4
const int dirPin5 = 4;  // Direction pin for stepper 5
const int stepPin5 = 5; // Step pin for stepper 5
const int dirPin6 = 6;  // Direction pin for stepper 6
const int stepPin6 = 7; // Step pin for stepper 6

// Stepper motor settings
const int stepsPerRevolution = 516; // Number of steps per full revolution for the motors
const int rpm = 10;                 // Motor speed in revolutions per minute (RPM)
const long delayPerStep = (60L * 1000L * 1000L) / (stepsPerRevolution * rpm); // Delay per step (microseconds)

// Sensor setup
int Right_Sensor = A0;      // Analog pin for the sensor
int Right_Sensor_Read;      // Variable to store sensor readings

void setup() {
  Serial.begin(9600);       // Initialize serial communication
  AFMS.begin();             // Initialize the motor shield
  strip.begin();            // Initialize the NeoPixel strip
  strip.setBrightness(10);  // Set LED brightness to a low value
  strip.clear();            // Turn off all LEDs initially
  strip.show();
  setDefaultWhite();        // Set all LEDs to default white color

  // Configure pins for external stepper motors as OUTPUT
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

  // Configure sensor pin
  pinMode(Right_Sensor, INPUT);
}

// Function to set all LEDs to white color
void setDefaultWhite() {
  strip.fill(strip.Color(255, 255, 255)); // Fill with white color
  strip.show(); // Update the LEDs
}

// Function to turn NeoPixel LEDs green sequentially
void turnGreen() {
  for (int i = 0; i < LED_COUNT; i++) {
    strip.setPixelColor(i, 0, 255, 0); // Set the current pixel to green
    strip.show(); // Update the LEDs
    delay(greenDelay); // Delay for the next pixel
  }
}

// Function to flash all LEDs blue for a short duration
void flashBlue() {
  strip.fill(strip.Color(0, 0, 255)); // Set all LEDs to blue
  strip.show(); // Update the LEDs
  delay(blueFlashInterval); // Keep blue for the defined interval
  strip.clear(); // Turn off all LEDs
  strip.show();
  delay(blueFlashInterval); // Wait before setting back to white
  setDefaultWhite(); // Return to default white
}

// Function to rotate an external stepper motor counterclockwise
void rotateExternalStepper(int dirPin, int stepPin) {
  digitalWrite(dirPin, LOW); // Set direction to counterclockwise
  for (int i = 0; i < stepsPerRevolution; i++) { // Loop for a full revolution
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(delayPerStep / 2);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(delayPerStep / 2);
  }
}

// Function to rotate an external stepper motor clockwise
void rotateExternalStepper2(int dirPin, int stepPin) {
  digitalWrite(dirPin, HIGH); // Set direction to clockwise
  for (int i = 0; i < stepsPerRevolution; i++) { // Loop for a full revolution
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(delayPerStep / 2);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(delayPerStep / 2);
  }
}

void loop() {
  int sensorValue = analogRead(A0); // Read value from the analog sensor
  Serial.println(sensorValue); // Print sensor value to Serial Monitor
  delay(100); // Small delay for stability

  // Check if any data is available from the Serial input
  if (Serial.available() > 0) {
    int receivedNumber = Serial.parseInt(); // Parse the received input as an integer

    // Perform actions based on the received number
    if (receivedNumber == 1) {
      turnGreen();
      rotateExternalStepper(dirPin1, stepPin1);
      unsigned long startTime = millis();
      while (millis() - startTime < 2000) { flashBlue(); }
    } else if (receivedNumber == 2) {
      turnGreen();
      rotateExternalStepper(dirPin2, stepPin2);
      unsigned long startTime = millis();
      while (millis() - startTime < 2000) { flashBlue(); }
    } else if (receivedNumber == 3) {
      turnGreen();
      rotateExternalStepper(dirPin3, stepPin3);
      unsigned long startTime = millis();
      while (millis() - startTime < 2000) { flashBlue(); }
    } else if (receivedNumber == 4) {
      turnGreen();
      rotateExternalStepper(dirPin4, stepPin4);
      unsigned long startTime = millis();
      while (millis() - startTime < 2000) { flashBlue(); }
    } else if (receivedNumber == 5) {
      turnGreen();
      rotateExternalStepper2(dirPin5, stepPin5); // Rotate stepper clockwise
      unsigned long startTime = millis();
      while (millis() - startTime < 2000) { flashBlue(); }
    } else if (receivedNumber == 6) {
      turnGreen();
      rotateExternalStepper(dirPin6, stepPin6);
      unsigned long startTime = millis();
      while (millis() - startTime < 2000) { flashBlue(); }
    }
    delay(50); // Short delay before next command
  }
}
