"""
NIAT Kit Motor Driver Module
Controls DC motors with speed and direction control.

Usage:
    from niat import Motor
    
    motor = Motor(motor=1)
    
    # Move forward at 50% speed
    motor.forward(speed=50)
    
    # Move backward at 75% speed
    motor.backward(speed=75)
    
    # Stop motor
    motor.stop()
    
    # Set custom speed (-100 to 100)
    motor.set_speed(speed=-50)  # Backward at 50%
"""

import board
import pwmio
import digitalio


# Motor A (Motor 1) Pin configuration
_M1_ENA_PIN = board.GPIO41   # Speed control (PWM)
_M1_IN1_PIN = board.GPIO42   # Direction 1
_M1_IN2_PIN = board.GPIO40   # Direction 2

# Motor B (Motor 2) Pin configuration
_M2_ENB_PIN = board.GPIO39   # Speed control (PWM)
_M2_IN3_PIN = board.GPIO45   # Direction 1
_M2_IN4_PIN = board.GPIO38   # Direction 2

# PWM Frequency
_PWM_FREQUENCY = 1000


class Motor:
    """
    A class to control DC motors.
    
    Supports forward, backward, and stop with variable speed (0-100).
    """
    
    def __init__(self, motor=1):
        """
        Initialize the motor driver.
        
        Args:
            motor: Motor number (1 or 2)
        """
        if motor not in [1, 2]:
            raise ValueError("Motor must be 1 or 2")
        
        self.motor = motor
        
        try:
            if motor == 1:
                self._speed_pin = pwmio.PWMOut(_M1_ENA_PIN, frequency=_PWM_FREQUENCY)
                self._dir1_pin = digitalio.DigitalInOut(_M1_IN1_PIN)
                self._dir2_pin = digitalio.DigitalInOut(_M1_IN2_PIN)
            else:
                self._speed_pin = pwmio.PWMOut(_M2_ENB_PIN, frequency=_PWM_FREQUENCY)
                self._dir1_pin = digitalio.DigitalInOut(_M2_IN3_PIN)
                self._dir2_pin = digitalio.DigitalInOut(_M2_IN4_PIN)
            
            # Set direction pins as outputs
            self._dir1_pin.direction = digitalio.Direction.OUTPUT
            self._dir2_pin.direction = digitalio.Direction.OUTPUT
            
            # Start stopped
            self.stop()
            
        except Exception:
            raise RuntimeError(
                f"Motor {motor} not found. Is the motor driver module plugged in?"
            )
    
    def forward(self, speed=50):
        """
        Move motor forward.
        
        Args:
            speed: Speed from 0 to 100
        """
        speed = max(0, min(100, speed))
        self._dir1_pin.value = True
        self._dir2_pin.value = False
        self._speed_pin.duty_cycle = int((speed / 100) * 65535)
    
    def backward(self, speed=50):
        """
        Move motor backward.
        
        Args:
            speed: Speed from 0 to 100
        """
        speed = max(0, min(100, speed))
        self._dir1_pin.value = False
        self._dir2_pin.value = True
        self._speed_pin.duty_cycle = int((speed / 100) * 65535)
    
    def stop(self):
        """
        Stop the motor.
        """
        self._dir1_pin.value = False
        self._dir2_pin.value = False
        self._speed_pin.duty_cycle = 0
    
    def set_speed(self, speed):
        """
        Set motor speed with direction.
        
        Args:
            speed: Speed from -100 (backward) to 100 (forward)
                  0 = stop
        """
        speed = max(-100, min(100, speed))
        
        if speed > 0:
            self.forward(speed)
        elif speed < 0:
            self.backward(abs(speed))
        else:
            self.stop()