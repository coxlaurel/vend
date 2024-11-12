import time
import serial
from rpi_ws281x import PixelStrip, Color

# LED configuration
LED_PIN = 6  # GPIO pin connected to the NeoPixels
LED_COUNT = 100  # Number of LED pixels
LED_BRIGHTNESS = 10  # Set brightness (0-255)
green_delay = 0.05  # Delay for turning LEDs green (in seconds)
blue_flash_interval = 0.6  # Flash interval in seconds for blue LEDs

# Initialize the NeoPixel strip
strip = PixelStrip(LED_COUNT, LED_PIN, brightness=LED_BRIGHTNESS)
strip.begin()

# Set up serial communication (adjust as needed)
ser = serial.Serial("/dev/ttyUSB0", 9600)  # Replace with your serial port


def turn_green():
    # Turn LEDs green one by one with delay
    for i in range(LED_COUNT):
        strip.setPixelColor(i, Color(0, 255, 0))  # Green color
        strip.show()
        time.sleep(green_delay)


def flash_blue():
    # Flash all LEDs blue
    strip.fill(Color(0, 0, 255))  # Blue color
    strip.show()
    time.sleep(blue_flash_interval)
    strip.clear()  # Turn off LEDs
    strip.show()
    time.sleep(blue_flash_interval)


def main():
    while True:
        if ser.in_waiting > 0:
            received_data = ser.readline().decode().strip()
            try:
                received_number = int(received_data)

                if received_number == 1:
                    print("Received 1 from Python!")
                    turn_green()  # Turn LEDs green one by one

                    start_time = time.time()
                    while time.time() - start_time < 2:
                        flash_blue()  # Flash LEDs blue every 0.6 seconds for 2 seconds

                elif received_number == 2:
                    print("Received 2 from Python!")
                    turn_green()  # Turn LEDs green one by one

                    start_time = time.time()
                    while time.time() - start_time < 2:
                        flash_blue()  # Flash LEDs blue every 0.6 seconds for 2 seconds

                else:
                    print("Invalid input. No motor found.")

            except ValueError:
                print("Invalid input. Please enter a number.")

            time.sleep(0.05)  # Small delay before loop repeats


if __name__ == "__main__":
    main()
