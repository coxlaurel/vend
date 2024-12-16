import kivy

from kivy.core.window import Window
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.clock import Clock
from kivy.metrics import sp

import button as bt

from config import FONT, SENSOR_THRESHOLD
from controller import read

Window.show_cursor = False
# Window.size = (480,800)
Window.fullscreen='auto'

class InsertCoinScreen(GridLayout, Screen):
    """
    Class to create insert coin screen.

    Attributes: 
        cols: An integer representing the number of columns
        screen_manager: An instance of screen manager
        sensor_event: A scheduled event action
    """
    def __init__(self, screen_manager, **kw):
        """
        Initialize an instance of insert coin screen.

        Args:
            screen_manager: An instance of screen manager
        """
        super(InsertCoinScreen, self).__init__(**kw)
        self.cols = 1
        self.rows = 2
        self.screen_manager = screen_manager
        self.sensor_event = None

        coin_label = Label(text='Please insert coin',
                           font_name=FONT,
                           font_size=sp(40),
                           color=(1, 1, 1, 1),
                           text_size=(480 * 0.8, None))
        self.add_widget(coin_label)

    def on_enter(self, *args):
        """
        Called when the screen becomes active.
        Starts periodic sensor checks.
        """
        # Schedule sensor checks every 0.5 seconds
        self.sensor_event = Clock.schedule_interval(self.check_sensor, 0.5)

    def on_leave(self, *args):
        """
        Called when the screen is no longer active.
        Stops periodic sensor checks.
        """
        # Unschedule sensor checks
        if hasattr(self, 'sensor_event'):
            self.sensor_event.cancel()

    def check_sensor(self, *args):
        """
        Periodically checks sensor data to determine if a coin was inserted.
        """
        try:
            sensor_reading = int(read())
            # print(f"Sensor Reading: {sensor_reading}")
            if sensor_reading < SENSOR_THRESHOLD:  # Adjust condition as needed
                self.go_to_main()
        except ValueError as e:
            print(f"Error reading sensor: {e}")

    def go_to_main(self):
        """
        Method to switch to the main screen.
        """
        self.screen_manager.current = "main"


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

        btn1 = bt.MakeButton("Oreos", 1, screen_manager=screen_manager)
        btn2 = bt.MakeButton("Kind Bar", 2, screen_manager=screen_manager)
        btn3 = bt.MakeButton("Lorna Doone", 3, screen_manager=screen_manager)
        btn4 = bt.MakeButton("Fruit Snack", 4, screen_manager=screen_manager)
        btn5 = bt.MakeButton("Hot Cocoa", 5, screen_manager=screen_manager)
        btn6 = bt.MakeButton("Rice Krispies", 6, screen_manager=screen_manager)

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
                           color=(1, 1, 1, 1)
                           )
        self.add_widget(vend_label)

    def on_enter(self, *args):
        """
        This method is called when the screen is displayed.
        Schedule a return to the main screen after 3 seconds.
        """
        Clock.schedule_once(self.go_to_coin, 13)

    def go_to_coin(self, _):
        """
        Method to switch back to the coin screen.
        """
        self.screen_manager.current = "coin"

class VENDApp(App):
    """
    Class to create vending machine interface.
    """
    def build(self):
        sm = ScreenManager()

        # Add screens to the ScreenManager
        sm.add_widget(InsertCoinScreen(name="coin", screen_manager=sm))
        sm.add_widget(MainScreen(name='main', screen_manager=sm))
        sm.add_widget(VendingScreen(name='vending', screen_manager=sm))

        return sm


if __name__ == '__main__':
    VENDApp().run()
