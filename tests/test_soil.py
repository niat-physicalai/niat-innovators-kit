"""
Soil Moisture Sensor Test
=========================
Run this to test and calibrate the soil sensor.

Instructions:
1. Run with sensor in AIR for dry reading
2. Run with sensor in WATER for wet reading
3. Run with sensor in SOIL to verify
"""

from niat import SoilSensor
import time

print("=" * 40)
print("Soil Moisture Sensor Test")
print("=" * 40)

# Initialize sensor
soil = SoilSensor()
print("[OK] Sensor initialized\n")

# Test 1: Single reading
print("Test 1: Single Reading")
moisture = soil.read_percent()
raw = soil.read_raw()
print(f"  Moisture: {moisture}%")
print(f"  Raw ADC:  {raw}")
print()

# Test 2: Continuous reading (10 seconds)
print("Test 2: Continuous Reading (10 sec)")
print("  Move sensor between air/water/soil...")
print()

for i in range(100):
    moisture = soil.read_percent()
    raw = soil.read_raw()
    bar = "#" * (moisture // 5)
    print(f"  {moisture:3d}% |{bar:<20}| raw={raw}")
    time.sleep(0.5)   
    # Check if plant needs water
    if moisture < 30:
        print("Dry! Water the plant!")
    else:
        print("Plant is happy!")

print()
print("=" * 40)
print("Test complete!")
print("=" * 40)
