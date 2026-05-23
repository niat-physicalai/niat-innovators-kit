"""
OLED Display Demo
=================
This example shows all the ways you can use the Screen.

The OLED display is a small screen that can show text,
numbers, and simple graphics.
"""

# Import the Screen class from the niat library
from niat import Screen

# Import time so we can add pauses between displays
import time


# Create a screen object to control the OLED display
screen = Screen()


# -----------------------------------------------------
# 1. PRINT TEXT
# -----------------------------------------------------
# Use print() to display any text message on the screen
screen.print("Hello NIAT!")
time.sleep(2)  # Wait 2 seconds so we can read it

# You can print any text you want
screen.print("Welcome!")
time.sleep(2)


# -----------------------------------------------------
# 2. SHOW A NUMBER
# -----------------------------------------------------
# Use show_number() to display a big number in the center
# Great for showing sensor readings or counters
screen.show_number(42)
time.sleep(2)

# Works with any number
screen.show_number(100)
time.sleep(2)

# Also works with decimal numbers
screen.show_number(3.14)
time.sleep(2)


# -----------------------------------------------------
# 3. DRAW A PROGRESS BAR
# -----------------------------------------------------
# Use draw_bar() to show progress or a percentage
# First number is the current value
# Second number is the maximum value

# Show 25% progress (25 out of 100)
screen.draw_bar(25, 100)
time.sleep(2)

# Show 50% progress (50 out of 100)
screen.draw_bar(50, 100)
time.sleep(2)

# Show 75% progress (75 out of 100)
screen.draw_bar(75, 100)
time.sleep(2)

# Show 100% complete
screen.draw_bar(100, 100)
time.sleep(2)


# -----------------------------------------------------
# 4. SHOW A MESSAGE WITH TITLE AND VALUE
# -----------------------------------------------------
# Use show_message() to display a label and a value
# Perfect for showing sensor readings with their names

# Show temperature reading
screen.show_message("Temperature", "28.5 C")
time.sleep(2)

# Show humidity reading
screen.show_message("Humidity", "65%")
time.sleep(2)

# Show soil moisture
screen.show_message("Soil", "Wet")
time.sleep(2)

# Show a countdown
for i in range(5, 0, -1):
    screen.show_message("Countdown", i)
    time.sleep(1)


# -----------------------------------------------------
# 5. CLEAR THE SCREEN
# -----------------------------------------------------
# Use clear() to blank the screen completely
screen.clear()
time.sleep(1)


# -----------------------------------------------------
# 6. PUTTING IT ALL TOGETHER
# -----------------------------------------------------
# Show a final message
screen.print("Demo Complete!")
time.sleep(2)
screen.clear()
