from niat import MicSensor
import time

mic = MicSensor()

print("Mic Test Started")

while True:
    print("------------------------")
    print("Percent:", mic.read_percent())
    print("Level:", mic.read_level())
    print("Loud:", mic.is_loud())
    time.sleep(1)