"""
Potentiometer (Knob) Complete Test
All functions demonstrated
"""

from niat import Knob
import time

print("=" * 50)
print("Knob - Complete Function Test")
print("=" * 50)

# Initialize
knob = Knob()
print("[OK] Knob initialized\n")

# Test 1: read_percent()
print("Test 1: read_percent()")
for i in range(3):
    percent = knob.read_percent()
    print(f"  Position: {percent}%")
    time.sleep(0.5)
print()

# Test 2: read_raw()
print("Test 2: read_raw()")
for i in range(3):
    raw = knob.read_raw()
    print(f"  Raw ADC: {raw}")
    time.sleep(0.5)
print()

# Test 3: read_voltage()
print("Test 3: read_voltage()")
for i in range(3):
    voltage = knob.read_voltage()
    print(f"  Voltage: {voltage}V")
    time.sleep(0.5)
print()

# Test 4: is_min()
print("Test 4: is_min() - Rotate to MINIMUM")
time.sleep(2)
is_min = knob.is_min()
percent = knob.read_percent()
print(f"  At minimum: {is_min} (Position: {percent}%)")
print()

# Test 5: is_max()
print("Test 5: is_max() - Rotate to MAXIMUM")
time.sleep(2)
is_max = knob.is_max()
percent = knob.read_percent()
print(f"  At maximum: {is_max} (Position: {percent}%)")
print()

# Test 6: is_middle()
print("Test 6: is_middle() - Rotate to MIDDLE")
time.sleep(2)
is_middle = knob.is_middle()
percent = knob.read_percent()
print(f"  At middle: {is_middle} (Position: {percent}%)")
print()

# Test 7: All functions together in a loop
print("Test 7: All Functions - Rotate Knob Continuously (15 sec)")
print()

end_time = time.monotonic() + 15
while time.monotonic() < end_time:
    percent = knob.read_percent()
    raw = knob.read_raw()
    voltage = knob.read_voltage()
    at_min = knob.is_min()
    at_max = knob.is_max()
    at_middle = knob.is_middle()
    
    # Status
    status = ""
    if at_min:
        status = "MIN"
    elif at_max:
        status = "MAX"
    elif at_middle:
        status = "MID"
    
    # Visual bar
    bar = "#" * (percent // 5)
    
    print(f"  {percent:3d}% |{bar:<20}| raw={raw:5d} | {voltage:.2f}V | {status}")
    time.sleep(0.3)

print()
print("=" * 50)
print("All tests complete!")
print("=" * 50)
print("\nFunctions tested:")
print("  ✓ read_percent() - Position 0-100%")
print("  ✓ read_raw() - Raw ADC value")
print("  ✓ read_voltage() - Voltage 0-3.3V")
print("  ✓ is_min() - Check minimum")
print("  ✓ is_max() - Check maximum")
print("  ✓ is_middle() - Check middle position")