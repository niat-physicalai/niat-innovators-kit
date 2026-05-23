"""
NIAT Kit Gas Sensor Module
Reads air quality from MQ135 gas sensor.

Usage:
    from niat import GasSensor

    gas = GasSensor()

    print(gas.read_raw())
    print(gas.read_quality())
    print(gas.read_level())

    print(gas.read_digital())
    print(gas.detected())

    if gas.is_polluted():
        print("Poor air quality")
"""

import board
import analogio
import digitalio


_AO_PIN = board.GPIO16
_DO_PIN = board.GPIO15


class GasSensor:
    def __init__(self):
        try:
            self._adc = analogio.AnalogIn(_AO_PIN)

            self._digital = digitalio.DigitalInOut(_DO_PIN)
            self._digital.direction = digitalio.Direction.INPUT

        except Exception as e:
            raise RuntimeError(
                f"Gas sensor not found: {e}"
            )

    def read_raw(self):
        return self._adc.value

    def read_quality(self):
        raw = self.read_raw()

        quality = 100 - int((raw / 65535) * 100)

        if quality < 0:
            quality = 0

        if quality > 100:
            quality = 100

        return quality

    def read_level(self):
        quality = self.read_quality()

        if quality >= 70:
            return "clean"
        elif quality >= 40:
            return "moderate"
        else:
            return "poor"

    def is_polluted(self):
        return self.read_quality() < 40

    def read_digital(self):
        return self._digital.value

    def detected(self):
        return not self._digital.value