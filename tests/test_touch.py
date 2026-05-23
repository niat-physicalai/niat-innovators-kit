"""
Touch Sensor Test
=================
Run this to test the capacitive touch sensor.

Instructions:
1. Touch the sensor pad
2. Watch the readings change in real-time
3. Press Ctrl+C to stop
"""

from niat import TouchPad
import time

print("=" * 50)
print("Touch Sensor Test")
print("=" * 50)

# Initialize sensor
touch = TouchPad()
print("[OK] Touch sensor initialized\n")

print("Touch the sensor pad...\n")
print("Press Ctrl+C to stop\n")

try:
    while True:
        state = touch.is_pressed()
        status = "TOUCHED" if state else "NOT TOUCHED"
        
        # Visual indicator
        indicator = "█" if state else "○"
        
        print(f"  {indicator} {status} | Raw: {state}")
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\n\nTest stopped!")