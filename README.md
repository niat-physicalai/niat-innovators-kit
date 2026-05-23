# NIAT Kit Firmware

Python-first educational firmware for the NIAT ESP32-S3 IoT Kit.

## Philosophy

Students learn Python concepts through physical hardware interaction.  
No GPIO, I2C, ADC, or PWM terms are ever exposed to students.

## Installation

1. Install CircuitPython on your ESP32-S3
2. Copy the `niat/` folder to your CIRCUITPY drive
3. Copy required Adafruit libraries to `lib/` folder

### Required Libraries

- `adafruit_neopixel`
- `adafruit_displayio_ssd1306`
- `adafruit_display_text`
- `adafruit_display_shapes`

## Quick Start

```python
from niat import LED, Screen

# Blink the LED
led = LED()
led.blink(color="red", count=3)

# Show message on screen
screen = Screen()
screen.print("Hello NIAT!")
```

## Project Structure

```
niat-kit-firmware/
├── niat/              # Core library modules
│   ├── __init__.py    # Main exports
│   ├── led.py         # LED control
│   ├── screen.py      # OLED display
│   ├── _board.py      # Pin definitions (internal)
│   └── _errors.py     # Error messages (internal)
├── examples/          # Working code examples
├── tests/             # Module test files
├── projects/          # Student project templates
├── docs/              # API documentation
└── context/           # AI agent context files
```

## Available Modules

| Module | Class | Description |
|--------|-------|-------------|
| led.py | `LED` | NeoPixel LED control |
| screen.py | `Screen` | OLED display (128x64) |

### Coming Soon

| Module | Class | Description |
|--------|-------|-------------|
| sensors.py | `TempSensor` | SHT31 temperature & humidity |
| sensors.py | `LightSensor` | VEML6030 ambient light |
| sensors.py | `SoilSensor` | Capacitive soil moisture |
| sensors.py | `RainSensor` | Rain detection |
| sensors.py | `GasSensor` | MQ135 air quality |
| inputs.py | `Button` | Push buttons |
| inputs.py | `TouchPad` | Capacitive touch |
| inputs.py | `Knob` | Potentiometer |
| sound.py | `Melody` | Buzzer tones |
| sound.py | `MicSensor` | I2S microphone |
| motor.py | `Motor` | L298N motor driver |
| relay.py | `Switch` | Relay module |

## Examples

### Blink LED

```python
from niat import LED
import time

led = LED()

while True:
    led.on("red")
    time.sleep(0.5)
    led.off()
    time.sleep(0.5)
```

### Display Sensor Data

```python
from niat import Screen

screen = Screen()
screen.show_message("Temperature", "28.5 C")
```

### Progress Bar

```python
from niat import Screen
import time

screen = Screen()

for i in range(0, 101, 10):
    screen.draw_bar(i, 100)
    time.sleep(0.5)
```

## Documentation

See [docs/API.md](docs/API.md) for complete API reference.

## Hardware Connections

See [context/pin_map.txt](context/pin_map.txt) for pin assignments.

| Component | Connection |
|-----------|------------|
| NeoPixel LED | Onboard (NEOPIXEL) |
| OLED Display | SDA: GPIO8, SCL: GPIO3 |

## Contributing

1. Follow the naming rules in `context/naming_rules.txt`
2. Use the module pattern from `context/modules.txt`
3. Add tests for new modules
4. Add examples for new features

## License

MIT License - NIAT Team