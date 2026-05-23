"""
Basic Development Board LED Test
"""

from niat import LED
import time

print("=" * 50)
print("Basic Board LED Test")
print("=" * 50)

led1 = LED(1)
led2 = LED(2)
led3 = LED(3)
led4 = LED(4)

print("Testing individual LEDs...")

led1.turn_on()
time.sleep(1)
led1.turn_off()

led2.turn_on()
time.sleep(1)
led2.turn_off()

led3.turn_on()
time.sleep(1)
led3.turn_off()

led4.turn_on()
time.sleep(1)
led4.turn_off()

print("Testing blink...")

led1.blink()
led2.blink()
led3.blink()
led4.blink()

print("Testing chase pattern...")

while True:
    led1.turn_on()
    time.sleep(0.2)
    led1.turn_off()

    led2.turn_on()
    time.sleep(0.2)
    led2.turn_off()

    led3.turn_on()
    time.sleep(0.2)
    led3.turn_off()

    led4.turn_on()
    time.sleep(0.2)
    led4.turn_off()