"""
NIAT Kit Rain Sensor Module
Reads rain detection from analog and digital outputs.

Usage:
    from niat import RainSensor

    rain = RainSensor()

    print(rain.read_intensity())
    print(rain.is_raining())
    print(rain.read_raw())
    print(rain.read_digital())
"""

import board
import analogio
import digitalio


_AO_PIN = board.GPIO12
_DO_PIN = board.GPIO13

# Custom PCB calibration
_DRY_VALUE = 33500
_WET_VALUE = 20000


class RainSensor:
    def __init__(self):
        try:
            self._adc = analogio.AnalogIn(_AO_PIN)

            self._digital = digitalio.DigitalInOut(_DO_PIN)
            self._digital.direction = digitalio.Direction.INPUT

        except Exception as e:
            raise RuntimeError(
                f"Rain sensor not found: {e}"
            )

    def read_raw(self):
        return self._adc.value

    def read_intensity(self):
        raw = self.read_raw()

        intensity = ((_DRY_VALUE - raw) / (_DRY_VALUE - _WET_VALUE)) * 100

        if intensity < 0:
            intensity = 0

        if intensity > 100:
            intensity = 100

        return int(intensity)

    def is_raining(self):
        return self.read_intensity() > 20

    def read_digital(self):
        return self._digital.value