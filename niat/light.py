"""
NIAT Kit Light Sensor Module

Uses VEML6030 ambient light sensor.

Current wiring:
    SDA -> GPIO8
    SCL -> GPIO3

Usage:
    from niat import LightSensor

    light = LightSensor()

    print(light.read_lux())
    print(light.read_percent())
    print(light.read_level())

    print(light.is_dark())
    print(light.is_bright())
"""

import board
import busio
import time

_SDA_PIN = board.GPIO8
_SCL_PIN = board.GPIO3
_ADDRESS = 0x48

_ALS_CONF = 0x00
_ALS_DATA = 0x04


class LightSensor:
    def __init__(self):
        try:
            self.i2c = busio.I2C(_SCL_PIN, _SDA_PIN)

            while not self.i2c.try_lock():
                pass

            devices = self.i2c.scan()

            if _ADDRESS not in devices:
                self.i2c.unlock()
                raise RuntimeError("VEML6030 not detected")

            # Power on sensor
            config = bytearray([_ALS_CONF, 0x00, 0x00])
            self.i2c.writeto(_ADDRESS, config)

            self.i2c.unlock()
            time.sleep(0.2)

        except Exception as e:
            raise RuntimeError(
                f"Light sensor not found: {e}"
            )

    def _read_raw(self):
        register = bytearray([_ALS_DATA])
        data = bytearray(2)

        while not self.i2c.try_lock():
            pass

        self.i2c.writeto_then_readfrom(
            _ADDRESS,
            register,
            data
        )

        self.i2c.unlock()

        raw = data[0] | (data[1] << 8)
        return raw

    def read_lux(self):
        try:
            raw = self._read_raw()
            lux = raw * 0.0576
            return round(lux, 2)
        except Exception as e:
            print("Light read error:", e)
            return None

    def read_percent(self):
        lux = self.read_lux()

        if lux is None:
            return None

        percent = int((lux / 1000) * 100)

        if percent > 100:
            percent = 100

        if percent < 0:
            percent = 0

        return percent

    def read_level(self):
        lux = self.read_lux()

        if lux is None:
            return "error"

        if lux < 10:
            return "dark"
        elif lux < 100:
            return "dim"
        elif lux < 400:
            return "normal"
        elif lux < 800:
            return "bright"
        else:
            return "very bright"

    def is_dark(self):
        lux = self.read_lux()

        if lux is None:
            return False

        return lux < 50

    def is_bright(self):
        lux = self.read_lux()

        if lux is None:
            return False

        return lux > 400