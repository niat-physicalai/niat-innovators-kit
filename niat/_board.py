"""
NIAT Kit Board Configuration
Centralized pin definitions for all hardware modules.

This file is internal and should not be imported by students.
"""

import board


# ==============================================================================
# ONBOARD COMPONENTS
# ==============================================================================
NEOPIXEL_PIN = board.NEOPIXEL
BOOT_BUTTON_PIN = board.BOOT


# ==============================================================================
# OLED DISPLAY
# ==============================================================================
OLED_SDA_PIN = board.IO8
OLED_SCL_PIN = board.IO3
OLED_ADDRESS = 0x3C
OLED_WIDTH = 128
OLED_HEIGHT = 64


# ==============================================================================
# BASIC DEVELOPMENT BOARD
# ==============================================================================
LED1_PIN = board.IO2
LED2_PIN = board.IO4
LED3_PIN = board.IO5
LED4_PIN = board.IO6

BUTTON_SW1_PIN = board.IO7
BUTTON_SW2_PIN = board.IO15

BUZZER_PIN = board.IO46
POT_PIN = board.IO9


# ==============================================================================
# SENSORS
# ==============================================================================
TOUCH_PIN = board.IO10
SOIL_PIN = board.IO11
RAIN_AO_PIN = board.IO12
RAIN_DO_PIN = board.IO13
GAS_AO_PIN = board.IO14
GAS_DO_PIN = board.IO17


# ==============================================================================
# I2C SENSORS (Shared bus with OLED)
# ==============================================================================
SHT31_ADDRESS = 0x44
VEML6030_ADDRESS = 0x48


# ==============================================================================
# MOTOR DRIVER (L298N)
# ==============================================================================
MOTOR_ENA_PIN = board.IO41
MOTOR_IN1_PIN = board.IO42
MOTOR_IN2_PIN = board.IO43
MOTOR_ENB_PIN = board.IO44
MOTOR_IN3_PIN = board.IO45
MOTOR_IN4_PIN = board.IO38


# ==============================================================================
# RELAY MODULE
# ==============================================================================
RELAY1_PIN = board.IO16
RELAY2_PIN = board.IO18


# ==============================================================================
# LED MATRIX (8x8 WS2812B)
# ==============================================================================
LED_MATRIX_PIN = board.IO21
LED_MATRIX_COUNT = 64


# ==============================================================================
# I2S MICROPHONE
# ==============================================================================
MIC_BCLK_PIN = board.IO39
MIC_WS_PIN = board.IO40
MIC_DATA_PIN = board.IO47
