"""
Gas Sensor + OLED Display
Real-time air quality monitoring with progress bar & alerts
Alerts printed every 10 seconds
"""

from niat import GasSensor, OLED
import time


# Initialize sensor and display
gas = GasSensor()
screen = OLED()

print("Starting Gas Sensor Monitor...")
time.sleep(1)

# Alert timer
last_alert_time = 0
alert_interval = 10  # Print alert every 10 seconds


while True:
    # Read sensor data
    quality = gas.read_quality()
    level = gas.read_level()
    raw = gas.read_raw()
    current_time = time.monotonic()
    
    # Determine status
    if quality < 50:
        status = "POOR"
    elif quality < 70:
        status = "FAIR"
    else:
        status = "GOOD"
    
    # Display on OLED - NO CLEAR (prevents blinking)
    screen.show_message(
        f"Air Quality: {quality}%",
        f"Status: {status}"
    )
    
    # Alternative: Just progress bar with percentage
    # screen.progress_bar(value=quality)
    # screen.print(f"Quality: {quality}%", row=3)
    
    # Print alerts every 10 seconds to serial
    if current_time - last_alert_time >= alert_interval:
        if quality < 50:
            print(f"[ALERT] Air quality is POOR! Quality: {quality}%")
        else:
            print(f"Air quality is GOOD. Quality: {quality}%")
        
        last_alert_time = current_time
    
    # Debug output
    print(f"  Quality: {quality}%  |  Level: {level}  |  Status: {status}")
    
    time.sleep(1)