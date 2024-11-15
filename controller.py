import serial

from config import PORT, BAUDRATE

arduino = serial.Serial(port=PORT, baudrate=BAUDRATE, timeout=.1)

def write(x):
    """
    Function to write to serial monitor.

    Args:
        x: An integer representing the motor number
    """
    # arduino.write(bytes(str(x), 'utf-8'))
    pass


def read():
    """
    Function to read serial monitor lines.

    Returns:
        A string representing the info read form serial monitor. 
    """
    #line = arduino.readline().decode('utf-8').strip()
    pass
