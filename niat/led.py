"""
NIAT Kit LED Module

Controls LEDs on the Basic Development Board.

Current wiring:
    LED1 -> GPIO2
    LED2 -> GPIO3
    LED3 -> GPIO4
    LED4 -> GPIO5

Usage:
    from niat import LED

    led = LED(1)

    led.turn_on()
    led.turn_off()
    led.toggle()
    led.blink()

    print(led.is_on())
"""

import board
import digitalio
import time

_LED_PINS = {
    1: board.GPIO2,
    2: board.GPIO3,
    3: board.GPIO4,
    4: board.GPIO5,
}


class LED:
    def __init__(self, number=1):
        if number not in _LED_PINS:
            raise ValueError("LED number must be 1 to 4.")

        self.led = digitalio.DigitalInOut(_LED_PINS[number])
        self.led.direction = digitalio.Direction.OUTPUT
        self._state = False

    def turn_on(self):
        self.led.value = True
        self._state = True

    def turn_off(self):
        self.led.value = False
        self._state = False

    def toggle(self):
        self.led.value = not self.led.value
        self._state = self.led.value

    def blink(self, times=3, delay=0.3):
        for _ in range(times):
            self.turn_on()
            time.sleep(delay)
            self.turn_off()
            time.sleep(delay)

    def is_on(self):
        return self._state