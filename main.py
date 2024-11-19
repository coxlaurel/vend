import kivy

from kivy.core.window import Window
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.clock import Clock
from kivy.metrics import sp

import button as bt

from config import FONT

Window.size = (480,800)
Window.fullscreen='fake'

class MainScreen(GridLayout, Screen):
    """
    Class to create main vending option interface.

    Attributes:
        cols: An integer representing the number of columns
        rows: An integer representing the number of rows
    """
    def __init__(self, screen_manager, **kwargs):
        """
        Initialize an instance of Main Screen.

        Args:
            screen_manager: An instance of screen manager
        """
        super(MainScreen, self).__init__(**kwargs)
        self.cols = 2
        self.rows = 3

        btn1 = bt.MakeButton("Popcorn", 1, screen_manager=screen_manager)
        btn2 = bt.MakeButton("Chocolate", 2, screen_manager=screen_manager)
        btn3 = bt.MakeButton("Candy", 3, screen_manager=screen_manager)
        btn4 = bt.MakeButton("Twizzler", 4, screen_manager=screen_manager)
        btn5 = bt.MakeButton("Mike & Ike", 5, screen_manager=screen_manager)
        btn6 = bt.MakeButton("Tootsie Roll", 6, screen_manager=screen_manager)

        self.add_widget(btn1)
        self.add_widget(btn2)
        self.add_widget(btn3)
        self.add_widget(btn4)
        self.add_widget(btn5)
        self.add_widget(btn6)


class VendingScreen(GridLayout, Screen):
    """
    Class to create interface when actively vending item.

    Attributes: 
        cols: An integer representing the number of columns
        screen_manager: An instance of screen manager
    """
    def __init__(self, screen_manager, **kwargs):
        """
        Initialize an instance of vending screen.

        Args:
            screen_manager: An instance of screen manager
        """
        super(VendingScreen, self).__init__(**kwargs)
        self.cols = 1
        self.screen_manager = screen_manager

        vend_label = Label(text='Vending...',
                           font_name=FONT,
                           font_size=sp(60),
                           color=(1, 0, 1, 1)
                           )
        self.add_widget(vend_label)

    def on_enter(self, *args):
        """
        This method is called when the screen is displayed.
        Schedule a return to the main screen after 3 seconds.
        """
        Clock.schedule_once(self.go_to_main, 3)

    def go_to_main(self, _):
        """
        Method to switch back to the main screen.
        """
        self.screen_manager.current = "main"

class VendingApp(App):
    """
    Class to create vending machine interface.
    """
    def build(self):
        sm = ScreenManager()

        # Add screens to the ScreenManager
        sm.add_widget(MainScreen(name='main', screen_manager=sm))
        sm.add_widget(VendingScreen(name='vending', screen_manager=sm))

        return sm


if __name__ == '__main__':
    VendingApp().run()
