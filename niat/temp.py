"""
NIAT Kit Temperature Sensor Module

Uses SHT31 temperature and humidity sensor.

Current wiring:
    SDA -> GPIO8
    SCL -> GPIO3

Usage:
    from niat import TempSensor

    sensor = TempSensor()

    print(sensor.read_temperature())   # Celsius
    print(sensor.read_humidity())      # Percent
    print(sensor.read_both())          # (temperature, humidity)

    print(sensor.is_comfortable())     # True / False
    print(sensor.get_status())         # descriptive status
"""

import board
import busio
import adafruit_sht31d
import time

_SDA_PIN = board.GPIO8
_SCL_PIN = board.GPIO3
_ADDRESS = 0x44


class TempSensor:
    def __init__(self):
        try:
            i2c = busio.I2C(_SCL_PIN, _SDA_PIN)
            time.sleep(0.2)

            self._sensor = adafruit_sht31d.SHT31D(
                i2c,
                address=_ADDRESS
            )

            time.sleep(0.2)

        except Exception as e:
            raise RuntimeError(
                f"Temperature sensor not found: {e}"
            )

    def read_temperature(self):
        try:
            return round(self._sensor.temperature, 2)
        except Exception as e:
            print("Temperature read error:", e)
            return None

    def read_humidity(self):
        try:
            return round(self._sensor.relative_humidity, 2)
        except Exception as e:
            print("Humidity read error:", e)
            return None

    def read_both(self):
        temp = self.read_temperature()
        humidity = self.read_humidity()
        return (temp, humidity)

    def is_comfortable(self, temp_min=20, temp_max=28, humidity_max=60):
        temp = self.read_temperature()
        humidity = self.read_humidity()

        if temp is None or humidity is None:
            return False

        return temp_min <= temp <= temp_max and humidity <= humidity_max

    def get_status(self):
        temp = self.read_temperature()
        humidity = self.read_humidity()

        if temp is None or humidity is None:
            return {
                "temperature": None,
                "humidity": None,
                "temp_status": "error",
                "humidity_status": "error",
                "comfortable": False
            }

        if temp < 15:
            temp_status = "cold"
        elif temp < 20:
            temp_status = "cool"
        elif temp <= 28:
            temp_status = "comfortable"
        elif temp < 35:
            temp_status = "warm"
        else:
            temp_status = "hot"

        if humidity < 30:
            humidity_status = "dry"
        elif humidity <= 60:
            humidity_status = "comfortable"
        else:
            humidity_status = "humid"

        return {
            "temperature": temp,
            "humidity": humidity,
            "temp_status": temp_status,
            "humidity_status": humidity_status,
            "comfortable": self.is_comfortable()
        }