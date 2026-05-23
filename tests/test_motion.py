from niat.motion import MotionSensor
import time

motion = MotionSensor()

print("MPU6050 Test Started")

while True:
    print("--------------------")
    print("Acceleration:", motion.read_acceleration())
    print("Rotation:", motion.read_rotation())
    print("Temperature:", motion.read_temperature())
    print("Moving:", motion.is_moving())
    print("Tilted:", motion.is_tilted())
    time.sleep(1)