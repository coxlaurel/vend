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
        color: RGBA format for text color
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
        """
        super(MakeButton, self).__init__(**kwargs)
        self.text = name
        self.font_style = FONT
        self.color = (0,0,0,1)
        self.background_normal = "assets/images/film.png"
        self.background_down = "assets/images/red_bg.png"
        self.motor = motor
        self.font_size = size
        self.screen_manager = screen_manager

    def on_press(self):
        """
        A method to activate servo on button press.

        Returns:
            self.status: An integer 1 or 0 representing motor activation or not.
        """
        write(self.motor)

    def on_release(self):
        """
        Method to switch to vending screen.
        """
        self.screen_manager.transition = SwapTransition(duration=1)
        self.screen_manager.current = 'vending'
