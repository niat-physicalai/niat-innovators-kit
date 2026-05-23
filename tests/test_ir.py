"""
IR Sensor Test
==============
Run this to test the infrared sensor.

Instructions:
1. Pass your hand in front of the sensor
2. Watch the readings change
3. Press Ctrl+C to stop
"""

from niat import IRSensor
import time

print("=" * 50)
print("IR Sensor Test")
print("=" * 50)

# Initialize sensor
ir = IRSensor()
print("[OK] IR sensor initialized\n")

# Test 1: Single reading
print("Test 1: Single Reading")
detected = ir.is_detected()
status = "DETECTED" if detected else "CLEAR"
print(f"  Current state: {status}\n")

# Test 2: Continuous monitoring
print("Test 2: Continuous Monitoring (20 sec)")
print("  Move your hand in front of the sensor...\n")

end_time = time.monotonic() + 20
detection_count = 0

while time.monotonic() < end_time:
    detected = ir.is_detected()
    status = "DETECTED" if detected else "CLEAR"
    indicator = "●" if detected else "○"
    
    if detected:
        detection_count += 1
    
    print(f"  {indicator} {status}")
    time.sleep(0.2)

print()
print(f"  Objects detected: {detection_count} times")
print()
print("=" * 50)
print("Test complete!")
print("=" * 50)