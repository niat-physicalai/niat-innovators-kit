"""
Motor Driver Test
=================
Run this to test both motors.

WARNING: Motors will spin!
Make sure motors are not attached to propellers or gears during testing.
"""

from niat import Motor
import time

print("=" * 50)
print("Motor Driver Test")
print("=" * 50)

# Test Motor 1
print("\nTest 1: Motor 1")
motor1 = Motor(motor=1)
print("[OK] Motor 1 initialized")

print("  Forward at 50%...")
motor1.forward(speed=50)
time.sleep(2)

print("  Increasing to 100%...")
motor1.set_speed(speed=100)
time.sleep(2)

print("  Backward at 50%...")
motor1.backward(speed=50)
time.sleep(2)

print("  Stopping...")
motor1.stop()
time.sleep(1)

# Test Motor 2
print("\nTest 2: Motor 2")
motor2 = Motor(motor=2)
print("[OK] Motor 2 initialized")

print("  Forward at 50%...")
motor2.forward(speed=50)
time.sleep(2)

print("  Increasing to 100%...")
motor2.set_speed(speed=100)
time.sleep(2)

print("  Backward at 50%...")
motor2.backward(speed=50)
time.sleep(2)

print("  Stopping...")
motor2.stop()
time.sleep(1)

# Test set_speed with negative values
print("\nTest 3: set_speed() method")
print("  Forward 75%...")
motor1.set_speed(speed=75)
time.sleep(2)

print("  Backward 75%...")
motor1.set_speed(speed=-75)
time.sleep(2)

print("  Stop...")
motor1.set_speed(speed=0)

print()
print("=" * 50)
print("Test complete!")
print("=" * 50)