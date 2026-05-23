"""
NIAT Kit IR Sensor Module
Detects obstacles or proximity using infrared sensor.

Usage:
    from niat import IRSensor
    
    ir = IRSensor()
    
    # Check if object detected
    if ir.is_detected():
        print("Object detected!")
    
    # Read raw state
    state = ir.read()
"""

import board
import digitalio


# Pin configuration
_IR_PIN = board.GPIO1


class IRSensor:
    """
    A class to detect objects using infrared sensor.
    
    Returns True when object is detected, False when path is clear.
    """
    
    def __init__(self):
        """
        Initialize the IR sensor.
        """
        try:
            self._ir = digitalio.DigitalInOut(_IR_PIN)
            self._ir.direction = digitalio.Direction.INPUT
        except Exception:
            raise RuntimeError(
                "IR sensor not found. Is the IR module plugged in?"
            )
    
    def is_detected(self):
        """
        Check if an object is detected.
        
        Returns:
            bool: True if object detected, False if path is clear
        """
        return not self._ir.value
    
    def read(self):
        """
        Read the raw IR sensor state.
        
        Returns:
            bool: True if object detected, False if path is clear
        """
        return not self._ir.value