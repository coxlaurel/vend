import kivy
import serial

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.behaviors import ButtonBehavior

from kivy.config import Config
Config.set('input', '/dev/input/event5', 'ignore')
Config.set('input', 'mouse', 'mouse,disable_multitouch')  # Disable multitouch for mouse


arduino = serial.Serial(port='/dev/ttyACM1', baudrate=9600, timeout=.1)


def write(x):
    """
    Function to write to serial monitor.

    Args:
        x: An integer representing the motor number
    """
    # print("writing...")
    arduino.write(bytes(str(x), 'utf-8'))


class MakeButton(Button, ButtonBehavior):
    """
    Class to create a button.

    Attributes:
        text: A string representing the name
        motor: An integer representing the corresponding motor number
        font_size: An integer representing the font size
    """
    def __init__(self, name, motor, size=30, **kwargs):
        """
        Function to initialize a button.

        Args:
            name: A string representing the name
            motor: An integer representing the corresponding motor number
            size: An integer representing the font size. Default = 30
        """
        super(MakeButton, self).__init__(**kwargs)
        self.status = 0
        self.text = name
        self.motor = motor
        self.font_size = size

    def on_press(self):
        """
        A function to activate servo on button press.
        """
        self.status = 1
        if self.status == 1:
            write(self.motor)


class MainScreen(GridLayout):
    """
    Class to create main vending option interface.

    Attributes:
        cols: An integer representing the number of columns
    """
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.cols = 2

        btn1 = MakeButton("Popcorn", 1)
        btn2 = MakeButton("Chocolate", 2)

        self.add_widget(btn1)
        self.add_widget(btn2)


class MyApp(App):
    """
    Class for build functions of app.
    """
    def build(self):
        return MainScreen()


if __name__ == '__main__':
    MyApp().run()
