from niat import GasSensor
import time

gas = GasSensor()

print("MQ135 Gas Sensor Test Started")
print("-----------------------------")

while True:
    print(
        "Raw:", gas.read_raw(),
        "| Quality:", gas.read_quality(), "%",
        "| Level:", gas.read_level(),
        "| D0:", gas.read_digital(),
        "| Gas Detected:", gas.detected()
    )

    time.sleep(1)