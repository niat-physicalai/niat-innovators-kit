"""
Rain Sensor Test
================
Run this to test the rain sensor.

Instructions:
1. Keep sensor dry for baseline
2. Wet the sensor or spray water to see readings change
3. Watch real-time intensity readings
"""

from niat import RainSensor
import time

print("=" * 50)
print("Rain Sensor Test")
print("=" * 50)

# Initialize sensor
rain = RainSensor()
print("[OK] Rain sensor initialized\n")

# Test 1: Single reading
print("Test 1: Single Reading")
intensity = rain.read_intensity()
digital = rain.is_raining()
raw = rain.read_raw()
print(f"  Intensity: {intensity}%")
print(f"  Raining (Digital): {digital}")
print(f"  Raw ADC: {raw}")
print()

# Test 2: Continuous reading (20 seconds)
print("Test 2: Continuous Reading (20 sec)")
print("  Spray water on sensor to see readings change...\n")

for i in range(100):
    intensity = rain.read_intensity()
    digital = rain.is_raining()
    raw = rain.read_raw()
    bar = "#" * (intensity // 5)
    status = "RAINING" if digital else "DRY"
    print(f"  {intensity:3d}% |{bar:<20}| {status:7s} | raw={raw}")
    time.sleep(1)

print()
print("=" * 50)
print("Test complete!")
print("=" * 50)