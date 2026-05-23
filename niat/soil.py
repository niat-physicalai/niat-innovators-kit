"""
NIAT Kit Soil Moisture Sensor Module
Reads soil moisture level from capacitive sensor.

Usage:
    from niat import SoilSensor
    
    soil = SoilSensor()
    
    # Read moisture percentage (0-100)
    moisture = soil.read_percent()
    print(f"Moisture: {moisture}%")
    
    # Check if plant needs water
    if moisture < 30:
        print("Dry! Water the plant!")
    else:
        print("Plant is happy!")
    
    # Get raw value for calibration
    
    raw = soil.read_raw()
"""

import board
import analogio


# Pin configuration
_SOIL_PIN = board.IO11

# Calibration values (typical for capacitive sensor v1.2)
_DRY_VALUE = 50000
_WET_VALUE = 20000


class SoilSensor:
    """
    A class to read soil moisture levels.
    
    Returns moisture as a percentage (0% = dry, 100% = wet).
    """
    
    def __init__(self):
        """
        Initialize the soil moisture sensor.
        """
        try:
            self._adc = analogio.AnalogIn(_SOIL_PIN)
        except Exception:
            raise RuntimeError(
                "Soil sensor not found. Is the moisture probe plugged in?"
            )
    
    def read_percent(self):
        """
        Read the current soil moisture level.
        
        Returns:
            int: Moisture percentage from 0 (dry) to 100 (wet)
        """
        raw = self._adc.value
        
        # Convert raw value to percentage (inverted: lower value = wetter)
        percent = ((_DRY_VALUE - raw) / (_DRY_VALUE - _WET_VALUE)) * 100
        
        # Clamp to 0-100 range
        return max(0, min(100, int(percent)))
    
    def read_raw(self):
        """
        Read the raw sensor value (for calibration).
        
        Returns:
            int: Raw ADC value
        """
        return self._adc.value
