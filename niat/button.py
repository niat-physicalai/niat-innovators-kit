"""
NIAT Kit Push Button Module
Detects button presses and releases.

Usage:
    from niat import Button
    
    btn = Button(button=1)
    
    # Check if button is pressed
    if btn.is_pressed():
        print("Button pressed!")
    
    # Wait for button press
    btn.wait_press()
    print("Button was pressed!")
"""

import board
import digitalio
import time


# Pin configuration
_BTN1_PIN = board.GPIO7   # Button 1 (SW1)
_BTN2_PIN = board.GPIO15  # Button 2 (SW2)

# Debounce delay (in seconds)
_DEBOUNCE_TIME = 0.02


class Button:
    """
    A class to detect button presses.
    
    Supports 2 independent buttons with debouncing.
    """
    
    def __init__(self, button=1):
        """
        Initialize the push button.
        
        Args:
            button: Button number (1 or 2)
        """
        if button not in [1, 2]:
            raise ValueError("Button must be 1 or 2")
        
        self.button = button
        pin = _BTN1_PIN if button == 1 else _BTN2_PIN
        
        try:
            self._btn = digitalio.DigitalInOut(pin)
            self._btn.direction = digitalio.Direction.INPUT
            self._btn.pull = digitalio.Pull.UP  # Pull-up resistor
            self._last_state = False
            self._last_press_time = 0
        except Exception:
            raise RuntimeError(
                f"Button {button} not found. Is the button connected?"
            )
    
    def is_pressed(self):
        """
        Check if the button is currently pressed.
        
        Returns:
            bool: True if pressed, False if not pressed
        """
        return not self._btn.value  # Inverted (pull-up)
    
    def wait_press(self, timeout=None):
        """
        Wait for the button to be pressed.
        
        Args:
            timeout: Maximum time to wait in seconds (None = wait forever)
        
        Returns:
            bool: True if button was pressed, False if timeout
        """
        start_time = time.monotonic()
        
        while True:
            if self.is_pressed():
                time.sleep(_DEBOUNCE_TIME)  # Debounce
                if self.is_pressed():
                    return True
            
            if timeout and (time.monotonic() - start_time) > timeout:
                return False
            
            time.sleep(0.01)
    
    def wait_release(self):
        """
        Wait for the button to be released after a press.
        """
        while self.is_pressed():
            time.sleep(0.01)
        time.sleep(_DEBOUNCE_TIME)
    
    def get_press_duration(self):
        """
        Measure how long the button was held.
        
        Returns:
            float: Duration in seconds
        """
        self.wait_press()
        press_time = time.monotonic()
        self.wait_release()
        duration = time.monotonic() - press_time
        return duration