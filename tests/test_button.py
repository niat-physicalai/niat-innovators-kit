"""
Push Button Test
================
Run this to test both push buttons.

Instructions:
1. Press button 1 and watch readings
2. Press button 2 and watch readings
3. Hold button to measure press duration
4. Press Ctrl+C to stop
"""

from niat import Button
import time

print("=" * 50)
print("Push Button Test")
print("=" * 50)

# Initialize both buttons
btn1 = Button(button=1)
btn2 = Button(button=2)
print("[OK] Both buttons initialized\n")

# Test 1: Check initial state
print("Test 1: Initial State")
print(f"  Button 1: {'PRESSED' if btn1.is_pressed() else 'RELEASED'}")
print(f"  Button 2: {'PRESSED' if btn2.is_pressed() else 'RELEASED'}")
print()

# Test 2: Wait for button press
print("Test 2: Wait for Button Press")
print("  Press button 1...")
btn1.wait_press()
print("  Button 1 was pressed!")
btn1.wait_release()
print("  Button 1 was released")
time.sleep(0.5)

print("  Press button 2...")
btn2.wait_press()
print("  Button 2 was pressed!")
btn2.wait_release()
print("  Button 2 was released")
time.sleep(0.5)

# Test 3: Measure press duration
print("\nTest 3: Measure Press Duration")
print("  Press button 1 and hold for a few seconds...")
duration = btn1.get_press_duration()
print(f"  Button held for {duration:.2f} seconds")
time.sleep(0.5)

print("  Press button 2 and hold for a few seconds...")
duration = btn2.get_press_duration()
print(f"  Button held for {duration:.2f} seconds")
time.sleep(0.5)

# Test 4: Continuous monitoring
print("\nTest 4: Continuous Monitoring (10 sec)")
print("  Press either button...\n")

end_time = time.monotonic() + 10
while time.monotonic() < end_time:
    btn1_state = "PRESSED" if btn1.is_pressed() else "RELEASED"
    btn2_state = "PRESSED" if btn2.is_pressed() else "RELEASED"
    print(f"  Button 1: {btn1_state}  |  Button 2: {btn2_state}")
    time.sleep(0.2)

print()
print("=" * 50)
print("Test complete!")
print("=" * 50)