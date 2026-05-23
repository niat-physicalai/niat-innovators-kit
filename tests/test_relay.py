"""
Relay Module Test - Simultaneous Control
==========================================
Turns both relays on and off simultaneously
with 3 second intervals in a continuous loop.
"""

from niat import Switch
import time

print("=" * 50)
print("Relay Module Test - Simultaneous Control")
print("=" * 50)

# Initialize both relays
relay1 = Switch(channel=1)
relay2 = Switch(channel=2)
print("[OK] Both relays initialized\n")

print("Starting loop - Press Ctrl+C to stop\n")

try:
    while True:
        # Turn both ON
        print("Turning ON both relays...")
        relay1.on()
        relay2.on()
        print(f"  Channel 1: {'ON' if relay1.is_on() else 'OFF'}")
        print(f"  Channel 2: {'ON' if relay2.is_on() else 'OFF'}")
        time.sleep(3)
        
        # Turn both OFF
        print("Turning OFF both relays...")
        relay1.off()
        relay2.off()
        print(f"  Channel 1: {'ON' if relay1.is_on() else 'OFF'}")
        print(f"  Channel 2: {'ON' if relay2.is_on() else 'OFF'}")
        time.sleep(3)

except KeyboardInterrupt:
    print("\n\nTest stopped!")
    relay1.off()
    relay2.off()
    print("Both relays turned off for safety")