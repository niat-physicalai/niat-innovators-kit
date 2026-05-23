"""
Temperature & Humidity Sensor Test
"""

from niat import TempSensor
import time

print("=" * 50)
print("SHT31 Temperature & Humidity Sensor Test")
print("=" * 50)

try:
    sensor = TempSensor()
    print("[OK] SHT31 sensor initialized\n")
except Exception as e:
    print("[ERROR]", e)
    raise

print("Test 1: Single Reading")
temperature = sensor.read_temperature()
humidity = sensor.read_humidity()

if temperature is not None and humidity is not None:
    print(f"Temperature: {temperature}°C")
    print(f"Humidity:    {humidity}%")
else:
    print("Failed to read sensor")

print()

print("Test 2: Read Both")
temp, hum = sensor.read_both()

if temp is not None and hum is not None:
    print(f"Temp: {temp}°C | Humidity: {hum}%")
else:
    print("Failed to read")

print()

print("Test 3: Comfort Check")
print("Comfortable:", sensor.is_comfortable())

print()

print("Test 4: Detailed Status")
status = sensor.get_status()

print(f"Temperature: {status['temperature']}°C ({status['temp_status']})")
print(f"Humidity: {status['humidity']}% ({status['humidity_status']})")
print(f"Overall Comfortable: {status['comfortable']}")

print()

print("Test 5: Continuous Monitoring")
print()

end_time = time.monotonic() + 20

while time.monotonic() < end_time:
    temp = sensor.read_temperature()
    humidity = sensor.read_humidity()

    if temp is not None and humidity is not None:
        comfort = sensor.is_comfortable()
        status = "✓" if comfort else "✗"

        print(
            f"{status} Temp: {temp:5.1f}°C | "
            f"Humidity: {humidity:5.1f}% | "
            f"Comfort: {comfort}"
        )
    else:
        print("Waiting for sensor...")

    time.sleep(1)

print()
print("=" * 50)
print("Test Complete")
print("=" * 50)