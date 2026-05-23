# OLED Complete Feature Test
# Tests ALL available functions

from niat import OLED
import time

screen = OLED()

# ========== 1. PRINT TEXT ==========
screen.clear()
screen.print("=== TEXT TEST ===")
time.sleep(1)

screen.clear()
screen.print("Line 1: Hello!")
screen.print("Line 2: Auto row")
screen.print("Line 3: NIAT Kit")
time.sleep(2)

screen.clear()
screen.print("Row 1", row=1)
screen.print("Row 4", row=4)
screen.print("Col 10", row=2, col=10)
time.sleep(2)

# ========== 2. SHOW NUMBER ==========
screen.clear()
screen.print("=== NUMBER TEST ===")
time.sleep(1)

screen.show_number(42)
time.sleep(1.5)

screen.show_number(3.14)
time.sleep(1.5)

screen.show_number(-99)
time.sleep(1.5)

# ========== 3. SHOW MESSAGE ==========
screen.clear()
screen.print("=== MESSAGE TEST ===")
time.sleep(1)

screen.show_message("Temperature", "28.5 C", "Humidity", "65%")
time.sleep(2)

screen.show_message("NIAT Kit", "Version 1.0")
time.sleep(2)

# ========== 4. ICONS ==========
screen.clear()
screen.print("=== ICON TEST ===")
time.sleep(1)

icons = ["smile", "heart", "star", "arrow_up", "checkmark", "cross", "warning", "music"]
for icon in icons:
    screen.show_icon(icon)
    time.sleep(1)

# ========== 5. DRAWING ==========
screen.clear()
screen.print("=== DRAW TEST ===")
time.sleep(1)

screen.clear()
screen.draw_box()
time.sleep(1.5)

screen.clear()
screen.draw_box(x=20, y=10, width=80, height=40)
time.sleep(1.5)

screen.clear()
screen.draw_line(direction="horizontal")
time.sleep(1)
screen.draw_line(direction="vertical")
time.sleep(1.5)

# ========== 6. PROGRESS BAR ==========
screen.clear()
screen.print("=== PROGRESS TEST ===")
time.sleep(1)

screen.clear()
for i in range(0, 101, 5):
    screen.progress_bar(i, label_text="Loading...")
    time.sleep(0.1)
time.sleep(1)

# ========== 7. FONT SIZE ==========
screen.clear()
screen.print("=== FONT TEST ===")
time.sleep(1)

screen.clear()
screen.set_font(size="small")
screen.print("Small font text")
time.sleep(1.5)

screen.clear()
screen.set_font(size="big")
screen.print("Big font")
time.sleep(1.5)

screen.set_font(size="small")

# ========== 8. INVERT ==========
screen.clear()
screen.print("=== INVERT TEST ===")
time.sleep(1)

screen.clear()
screen.print("Normal mode")
time.sleep(1)

screen.invert()
screen.print("Inverted!", row=3)
time.sleep(2)

screen.normal()
screen.clear()
screen.print("Back to normal")
time.sleep(1.5)

# ========== 9. BRIGHTNESS ==========
screen.clear()
screen.print("=== BRIGHTNESS ===")
time.sleep(1)

screen.clear()
screen.print("Dimming...")
for level in range(10, -1, -1):
    screen.brightness(level)
    time.sleep(0.3)

screen.print("Brightening...", row=3)
for level in range(0, 11):
    screen.brightness(level)
    time.sleep(0.3)
time.sleep(1)

# ========== 10. SCROLL TEXT ==========
screen.clear()
screen.print("=== SCROLL TEST ===")
time.sleep(1)

screen.clear()
screen.scroll_text("Hello NIAT Innovators!", speed=3)
time.sleep(0.5)

# ========== 11. COUNTDOWN ==========
screen.clear()
screen.print("=== COUNTDOWN ===")
time.sleep(1)

screen.countdown(from_number=5, message="Done!")
time.sleep(1)

# ========== COMPLETE ==========
screen.clear()
screen.show_message("All Tests", "Complete!", "", "Well Done!")
time.sleep(3)

screen.clear()
screen.show_icon("checkmark")