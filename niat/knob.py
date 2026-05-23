"""
NIAT Kit Potentiometer Module
Reads analog input from a rotary potentiometer.

Usage:
    from niat import Knob
    
    knob = Knob()
    
    # Read position as percentage (0-100)
    position = knob.read_percent()
    print(f"Position: {position}%")
    
    # Read raw analog value
    raw = knob.read_raw()
    
    # Check if at minimum or maximum
    if knob.is_min():
        print("At minimum position")
    
    if knob.is_max():
        print("At maximum position")
"""

import board
import analogio


# Pin configuration
_KNOB_PIN = board.GPIO9


class Knob:
    """
    A class to read rotary potentiometer input.
    
    Returns position as a percentage (0% = minimum, 100% = maximum).
    """
    
    def __init__(self):
        """
        Initialize the potentiometer.
        """
        try:
            self._knob = analogio.AnalogIn(_KNOB_PIN)
        except Exception:
            raise RuntimeError(
                "Potentiometer not found. Is the knob module plugged in?"
            )
    
    def read_percent(self):
        """
        Read the potentiometer position as a percentage.
        
        Returns:
            int: Position from 0 (minimum) to 100 (maximum)
        """
        raw = self._knob.value
        # Convert 16-bit ADC (0-65535) to 0-100
        percent = int((raw / 65535) * 100)
        return percent
    
    def read_raw(self):
        """
        Read the raw analog value from potentiometer.
        
        Returns:
            int: Raw ADC value (0-65535)
        """
        return self._knob.value
    
    def read_voltage(self):
        """
        Read the voltage at the potentiometer.
        
        Returns:
            float: Voltage from 0.0V to 3.3V
        """
        raw = self._knob.value
        # ESP32 uses 3.3V reference
        voltage = (raw / 65535) * 3.3
        return round(voltage, 2)
    
    def is_min(self, threshold=10):
        """
        Check if potentiometer is at minimum position.
        
        Args:
            threshold: Percentage threshold (default 10%)
        
        Returns:
            bool: True if position <= threshold
        """
        return self.read_percent() <= threshold
    
    def is_max(self, threshold=90):
        """
        Check if potentiometer is at maximum position.
        
        Args:
            threshold: Percentage threshold (default 90%)
        
        Returns:
            bool: True if position >= threshold
        """
        return self.read_percent() >= threshold
    
    def is_middle(self, range_percent=10):
        """
        Check if potentiometer is at middle position.
        
        Args:
            range_percent: Range around center (default 10%)
        
        Returns:
            bool: True if position within center range
        """
        pos = self.read_percent()
        return 50 - range_percent <= pos <= 50 + range_percent