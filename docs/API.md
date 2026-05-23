# NIAT Kit API Reference

Complete API documentation for the NIAT Kit Python library.

---

## Table of Contents

1. [LED](#led)
2. [Screen](#screen)

---

## LED

Control the onboard NeoPixel LED.

### Import

```python
from niat import LED
```

### Creating an LED

```python
led = LED()
```

### Methods

#### `on(color="white")`

Turn the LED on with the specified color.

**Parameters:**
- `color` (str or tuple): Color name or RGB tuple
  - Available colors: `"red"`, `"green"`, `"blue"`, `"white"`, `"yellow"`, `"orange"`, `"purple"`, `"cyan"`, `"pink"`, `"off"`
  - RGB tuple: `(255, 0, 0)` for red

**Example:**
```python
led.on()           # White (default)
led.on("red")      # Red
led.on((255, 0, 0)) # Also red (RGB)
```

---

#### `off()`

Turn the LED off.

**Example:**
```python
led.off()
```

---

#### `is_on()`

Check if the LED is currently on.

**Returns:** `True` if on, `False` if off

**Example:**
```python
if led.is_on():
    print("LED is on!")
```

---

#### `set_brightness(level)`

Set the LED brightness.

**Parameters:**
- `level` (int): Brightness from 0 (off) to 100 (full)

**Example:**
```python
led.set_brightness(50)  # 50% brightness
```

---

#### `blink(color="white", speed=0.5, count=3)`

Blink the LED a specified number of times.

**Parameters:**
- `color` (str): Color name
- `speed` (float): Seconds for each on/off cycle
- `count` (int): Number of blinks

**Example:**
```python
led.blink("red", speed=0.2, count=5)
```

---

#### `rainbow(duration=3.0, speed=0.05)`

Show a rainbow color cycle.

**Parameters:**
- `duration` (float): Total time in seconds
- `speed` (float): Color change speed

**Example:**
```python
led.rainbow(duration=5.0)
```

---

## Screen

Control the OLED display (128x64 pixels).

### Import

```python
from niat import Screen
```

### Creating a Screen

```python
screen = Screen()
```

### Methods

#### `print(text)`

Display text on the screen.

**Parameters:**
- `text`: Text to display (any value is converted to string)

**Example:**
```python
screen.print("Hello World!")
screen.print(42)
```

---

#### `clear()`

Clear all content from the screen.

**Example:**
```python
screen.clear()
```

---

#### `show_number(n)`

Display a large centered number.

**Parameters:**
- `n`: Number to display

**Example:**
```python
screen.show_number(42)
screen.show_number(3.14)
```

---

#### `draw_bar(value, max_value)`

Draw a horizontal progress bar.

**Parameters:**
- `value`: Current value
- `max_value`: Maximum value (determines fill percentage)

**Example:**
```python
screen.draw_bar(75, 100)   # 75% filled
screen.draw_bar(3, 10)     # 30% filled
```

---

#### `show_message(title, value)`

Display a title and value on two lines.

**Parameters:**
- `title`: Title text (top line, smaller)
- `value`: Value text (bottom line, larger)

**Example:**
```python
screen.show_message("Temperature", "28.5 C")
screen.show_message("Humidity", "65%")
screen.show_message("Score", 100)
```

---

## Error Handling

All modules raise friendly errors if hardware is not connected:

```python
try:
    screen = Screen()
except RuntimeError as e:
    print(e)  # "Screen not found. Is the OLED display plugged in?"
```

---

## Pin Connections

| Module | Pins |
|--------|------|
| LED (NeoPixel) | Onboard (board.NEOPIXEL) |
| Screen (OLED) | SDA: GPIO8, SCL: GPIO3 |

---

## Version

```python
import niat
print(niat.__version__)  # "1.0.0"
```
