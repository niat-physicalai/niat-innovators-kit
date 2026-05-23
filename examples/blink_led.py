"""
Blink LED Example
=================
This example shows how to use the LED class to blink
the onboard NeoPixel LED in different colors.

Great for beginners learning Python!
"""

# Import the LED class from the niat library
from niat import LED

# Import time for adding delays
import time


# Create an LED object
led = LED()


# -----------------------------------------------------
# Example 1: Simple On and Off
# -----------------------------------------------------
print("Example 1: Turn LED on and off")

# Turn the LED on (white color by default)
led.on()
time.sleep(1)  # Wait 1 second

# Turn the LED off
led.off()
time.sleep(1)


# -----------------------------------------------------
# Example 2: Different Colors
# -----------------------------------------------------
print("Example 2: Different colors")

# Turn on with red color
led.on("red")
time.sleep(1)

# Turn on with green color
led.on("green")
time.sleep(1)

# Turn on with blue color
led.on("blue")
time.sleep(1)

led.off()


# -----------------------------------------------------
# Example 3: Using the blink() method
# -----------------------------------------------------
print("Example 3: Blink automatically")

# Blink red 3 times, with 0.5 second speed
led.blink(color="red", speed=0.5, count=3)

# Blink yellow 5 times, faster
led.blink(color="yellow", speed=0.2, count=5)


# -----------------------------------------------------
# Example 4: Rainbow Effect
# -----------------------------------------------------
print("Example 4: Rainbow effect")

# Show rainbow colors for 3 seconds
led.rainbow(duration=3.0)


# -----------------------------------------------------
# Example 5: Brightness Control
# -----------------------------------------------------
print("Example 5: Brightness control")

led.on("white")

# Dim the LED (50% brightness)
led.set_brightness(50)
time.sleep(1)

# Full brightness
led.set_brightness(100)
time.sleep(1)

# Very dim (10% brightness)
led.set_brightness(10)
time.sleep(1)

# Turn off when done
led.off()
led.set_brightness(30)  # Reset brightness

print("Done!")
