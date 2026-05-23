"""
NIAT Kit Touch Sensor Module
Detects capacitive touch input.

Usage:
    from niat import TouchPad
    
    touch = TouchPad()
    
    # Check if touched
    if touch.is_pressed():
        print("Touch detected!")
    
    # Read raw state
    state = touch.read()
    print(f"Touch state: {state}")
"""

import board
import digitalio


# Pin configuration
_TOUCH_PIN = board.GPIO10


class TouchPad:
    """
    A class to detect capacitive touch input.
    
    Returns True when touched, False when not touched.
    """
    
    def __init__(self):
        """
        Initialize the touch sensor.
        """
        try:
            self._touch = digitalio.DigitalInOut(_TOUCH_PIN)
            self._touch.direction = digitalio.Direction.INPUT
        except Exception:
            raise RuntimeError(
                "Touch sensor not found. Is the touch pad plugged in?"
            )
    
    def is_pressed(self):
        """
        Check if the touch pad is currently pressed.
        
        Returns:
            bool: True if touched, False if not touched
        """
        return self._touch.value
    
    def read(self):
        """
        Read the raw touch state.
        
        Returns:
            bool: True if touched, False if not touched
        """
        return self._touch.value