"""
NIAT Kit Library
================
A student-friendly Python library for the NIAT ESP32-S3 IoT Kit.

Usage:
    from niat import LED, Screen
    
    led = LED()
    led.on("red")
    
    screen = Screen()
    screen.print("Hello!")
"""

from niat.led import LED
from niat.oled import Screen
from niat.soil import SoilSensor

# Version info
__version__ = "1.0.0"
__author__ = "NIAT Team"

# Public API
__all__ = [
    "LED",
    "Screen",
    "SoilSensor",
]
