from niat import LightSensor
import time

light = LightSensor()

print("VEML6030 Test Started")

while True:
    print(
        "Lux:", light.read_lux(),
        "| Percent:", light.read_percent(),
        "| Level:", light.read_level(),
        "| Dark:", light.is_dark(),
        "| Bright:", light.is_bright()
    )

    time.sleep(1)