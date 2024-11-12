import kivy
import serial

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager

import controller as ctl

PORT = '/dev/ttyACM1'
BAUDRATE = 9600
# arduino = serial.Serial(port=PORT, baudrate=BAUDRATE, timeout=.1)


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


def check_motor_active():
    """
    Function to verify whether or not motor is active.
    """
    pass


class MainScreen(GridLayout, Screen):
    """
    Class to create main vending option interface.

    Attributes:
        cols: An integer representing the number of columns
    """
    def __init__(self, screen_manager, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.cols = 2
        self.rows = 3

        btn1 = ctl.MakeButton("Popcorn", 1, screen_manager=screen_manager)
        btn2 = ctl.MakeButton("Chocolate", 2, screen_manager=screen_manager)
        btn3 = ctl.MakeButton("Candy", 3, screen_manager=screen_manager)
        btn4 = ctl.MakeButton("Twizzler", 4, screen_manager=screen_manager)
        btn5 = ctl.MakeButton("Mike & Ike", 5, screen_manager=screen_manager)
        btn6 = ctl.MakeButton("Tootsie Roll", 6, screen_manager=screen_manager)

        self.add_widget(btn1)
        self.add_widget(btn2)
        self.add_widget(btn3)
        self.add_widget(btn4)
        self.add_widget(btn5)
        self.add_widget(btn6)


class VendingScreen(GridLayout, Screen, Label):
    """
    Class to create interface when actively vending item.
    """
    def __init__(self, **kwargs):
        super(VendingScreen, self).__init__(**kwargs)
        self.cols = 1

        vend_label = Label(text='Vending...', color=(1, 0, 1, 1))
        self.add_widget(vend_label)


class VendingApp(App):
    """
    Class to create vending machine interface.
    """
    def build(self):
        sm = ScreenManager()

        # Add screens to the ScreenManager
        sm.add_widget(MainScreen(name='main', screen_manager=sm))
        sm.add_widget(VendingScreen(name='vending'))

        return sm


if __name__ == '__main__':
    VendingApp().run()
