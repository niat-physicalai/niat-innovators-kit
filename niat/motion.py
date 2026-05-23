"""
NIAT Kit Motion Sensor Module (MPU6050 IMU)

Provides motion sensing using MPU6050:
- 3-axis accelerometer
- 3-axis gyroscope
- onboard temperature sensor

Current wiring:
    SDA -> GPIO8
    SCL -> GPIO3

Usage:
    from niat import MotionSensor

    motion = MotionSensor()

    print(motion.read_acceleration())
    # (x, y, z) in m/s²

    print(motion.read_rotation())
    # (x, y, z) rotation values

    print(motion.read_temperature())
    # temperature in Celsius

    print(motion.is_moving())
    # True or False

    print(motion.is_tilted())
    # True or False
"""

import board
import busio
import time

_MPU6050_ADDR = 0x68
_PWR_MGMT_1 = 0x6B
_ACCEL_XOUT_H = 0x3B
_GYRO_XOUT_H = 0x43
_TEMP_OUT_H = 0x41


class MotionSensor:
    def __init__(self):
        try:
            self.i2c = busio.I2C(board.GPIO3, board.GPIO8)

            while not self.i2c.try_lock():
                pass

            devices = self.i2c.scan()

            if _MPU6050_ADDR not in devices:
                self.i2c.unlock()
                raise RuntimeError("MPU6050 not detected")

            # Wake up sensor
            self.i2c.writeto(
                _MPU6050_ADDR,
                bytes([_PWR_MGMT_1, 0x00])
            )

            self.i2c.unlock()
            time.sleep(0.1)

        except Exception as e:
            raise RuntimeError(
                f"MotionSensor initialization failed: {e}"
            )

    def _read_word(self, register):
        register_buffer = bytearray(1)
        register_buffer[0] = register

        data_buffer = bytearray(2)

        while not self.i2c.try_lock():
            pass

        self.i2c.writeto_then_readfrom(
            _MPU6050_ADDR,
            register_buffer,
            data_buffer
        )

        self.i2c.unlock()

        value = (data_buffer[0] << 8) | data_buffer[1]

        if value > 32767:
            value -= 65536

        return value

    def read_acceleration(self):
        x = self._read_word(_ACCEL_XOUT_H) / 16384.0 * 9.81
        y = self._read_word(_ACCEL_XOUT_H + 2) / 16384.0 * 9.81
        z = self._read_word(_ACCEL_XOUT_H + 4) / 16384.0 * 9.81

        return (
            round(x, 2),
            round(y, 2),
            round(z, 2),
        )

    def read_rotation(self):
        x = self._read_word(_GYRO_XOUT_H) / 131.0
        y = self._read_word(_GYRO_XOUT_H + 2) / 131.0
        z = self._read_word(_GYRO_XOUT_H + 4) / 131.0

        return (
            round(x, 2),
            round(y, 2),
            round(z, 2),
        )

    def read_temperature(self):
        temp_raw = self._read_word(_TEMP_OUT_H)
        temp = (temp_raw / 340.0) + 36.53
        return round(temp, 2)

    def is_moving(self, threshold=1.5):
        x, y, z = self.read_acceleration()

        if abs(x) > threshold:
            return True

        if abs(y) > threshold:
            return True

        if abs(z - 9.81) > threshold:
            return True

        return False

    def is_tilted(self, threshold=2.0):
        x, y, _ = self.read_acceleration()

        if abs(x) > threshold:
            return True

        if abs(y) > threshold:
            return True

        return False