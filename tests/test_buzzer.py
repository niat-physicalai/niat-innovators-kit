"""
Buzzer Test
===========
Run this to test the piezo buzzer.
"""

from niat import Melody
import time

print("=" * 50)
print("Buzzer Test")
print("=" * 50)

# Initialize buzzer
buzzer = Melody()
print("[OK] Buzzer initialized\n")

# Test 1: Single beep
print("Test 1: Single Beep")
buzzer.beep(count=1)
time.sleep(0.5)

# Test 2: Multiple beeps
print("Test 2: Multiple Beeps (3x)")
buzzer.beep(count=3, duration=0.1)
time.sleep(0.5)

# Test 3: Tone
print("Test 3: Tone (1000 Hz)")
buzzer.play_tone(frequency=1000, duration=0.5)
time.sleep(0.5)

# Test 4: Musical notes
print("Test 4: Musical Notes")
buzzer.play_note("C4", duration=0.3)
buzzer.play_note("D4", duration=0.3)
buzzer.play_note("E4", duration=0.3)
time.sleep(0.5)

# Test 5: Melody
print("Test 5: Melody (C4-E4-G4)")
buzzer.play_melody(["C4", "E4", "G4"], duration=0.3)
time.sleep(0.5)

# Test 6: Alert
print("Test 6: Alert Sound (2 sec)")
buzzer.alert(duration=2.0)
time.sleep(0.5)

print()
print("=" * 50)
print("Test complete!")
print("=" * 50)