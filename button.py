import kivy

from kivy.uix.button import Button
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.screenmanager import SwapTransition
from kivy.metrics import sp

from controller import write
from config import FONT

class MakeButton(Button, ButtonBehavior):
    """
    Class to create a button.

    Attributes:
        text: A string representing the name
        motor: An integer representing the corresponding motor number
        font_name: A string routing to desired font file
        font_size: An integer representing the font size
        background_color:
        screen_manager: An instance of screen manager
    """
    def __init__(self, name, motor, screen_manager, size=sp(30), **kwargs):
        """
        Initialize a button.

        Args:
            name: A string representing the name
            motor: An integer representing the corresponding motor number
            font_style: A string routing to font file
            screen_manager: An instance of screen manager
            size: An integer representing the font size. Default = 30
            color: A
        """
        super(MakeButton, self).__init__(**kwargs)
        self.status = 0
        self.text = name
        self.font_style = FONT
        self.background_color = (252/255, 163/255, 157/255, 1)
        self.motor = motor
        self.font_size = size
        self.screen_manager = screen_manager

    def on_press(self):
        """
        A method to activate servo on button press.

        Returns:
            self.status: An integer 1 or 0 representing motor activation or not.
        """
        self.status = 1
        # write(self.motor)

    def on_release(self):
        """
        Method to switch to vending screen.
        """
        self.screen_manager.transition = SwapTransition(duration=1)
        self.screen_manager.current = 'vending'
