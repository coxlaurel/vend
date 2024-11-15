import kivy

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager

import button as bt

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
