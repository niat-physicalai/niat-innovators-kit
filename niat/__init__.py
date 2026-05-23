"""
NIAT Kit Library
"""

from niat.led import LED
from niat.oled import OLED
from niat.soil import SoilSensor
from niat.gas import GasSensor
from niat.temp import TempSensor
from niat.rain import RainSensor
from niat.relay import Switch
from niat.touch import TouchPad
from niat.buzzer import Melody
from niat.button import Button
from niat.ir import IRSensor
from niat.light import LightSensor
from niat.motion import MotionSensor
from niat.matrix import PixelMatrix
from niat.knob import Knob
from niat.motor import Motor



# Version info
__version__ = "1.0.0"
__author__ = "NIAT Team"

# Public API
__all__ = [
    "LED",
    "OLED",
    "SoilSensor",
    "GasSensor",
    "TempSensor",
    "RainSensor",
    "Switch"
    "TouchPad",
    "Melody",
    "Button",
    "IRSensor",
    "LightSensor",
    "MotionSensor",
    "PixelMatrix",
    "Knob",
    "Motor"
]