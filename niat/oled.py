# ============================================================
#  NIAT Innovators Kit — OLED Display Module
#  File   : oled.py
#  Board  : ESP32-S3 + CircuitPython
#  Display: 128x64 SSD1306 (I2C, SDA=GPIO21, SCL=GPIO22)
#  Libs   : adafruit_ssd1306.mpy, adafruit_framebuf.mpy
#           (only 2 files needed in /lib folder)
# ============================================================
#
#  STUDENT USAGE EXAMPLES
#  -----------------------
#  from niat import OLED
#
#  screen = OLED()
#
#  screen.print("Hello World!")
#  screen.print("Score: 99", row=2)
#  screen.print("Hi", row=1, col=4)
#
#  screen.show_number(42)
#  screen.show_number(3.14)
#
#  screen.clear()
#
#  screen.draw_box()
#  screen.draw_line()
#  screen.draw_line(direction="vertical")
#
#  screen.show_icon("smile")
#  screen.show_icon("heart")
#  screen.show_icon("star")
#  screen.show_icon("arrow_up")
#  screen.show_icon("checkmark")
#  screen.show_icon("cross")
#  screen.show_icon("warning")
#  screen.show_icon("music")
#
#  screen.set_font(size="big")       # "small" or "big"
#  screen.invert()
#  screen.normal()
#  screen.brightness(level=5)        # 0 (off) to 10 (max)
#
#  screen.scroll_text("NIAT Innovators Kit!", speed=3)
#  screen.countdown(from_number=5)
#  screen.progress_bar(value=75)     # 0 to 100
#  screen.show_message("Line1", "Line2", "Line3", "Line4")
# ============================================================

import time
import busio
import board
import adafruit_ssd1306

# ── Hardware constants ────────────────────────────────────────
# YD-ESP32-S3 N16R8 I2C pins
# SDA = GPIO8, SCL = GPIO3
_SDA_PIN  = board.GPIO8
_SCL_PIN  = board.GPIO3
_I2C_ADDR = 0x3C
_WIDTH    = 128
_HEIGHT   = 64

# ── Pixel icon bitmaps (16x16) ────────────────────────────────
_ICONS = {
    "smile": [
        0b0000111111110000,
        0b0011000000001100,
        0b0100000000000010,
        0b1000000000000001,
        0b1001000000001001,
        0b1001000000001001,
        0b1000000000000001,
        0b1000000000000001,
        0b1000100000010001,
        0b1000011001100001,
        0b1000001111000001,
        0b0100000000000010,
        0b0011000000001100,
        0b0000111111110000,
        0b0000000000000000,
        0b0000000000000000,
    ],
    "heart": [
        0b0000000000000000,
        0b0001100001100000,
        0b0011110011110000,
        0b0111111111111000,
        0b0111111111111000,
        0b0011111111110000,
        0b0001111111100000,
        0b0000111111000000,
        0b0000011110000000,
        0b0000001100000000,
        0b0000000000000000,
        0b0000000000000000,
        0b0000000000000000,
        0b0000000000000000,
        0b0000000000000000,
        0b0000000000000000,
    ],
    "star": [
        0b0000000100000000,
        0b0000001110000000,
        0b0111111111111110,
        0b0011111111111100,
        0b0001111111111000,
        0b0000111010110000,
        0b0001100000001100,
        0b0011000000000110,
        0b0110000000000011,
        0b0100000000000001,
        0b0000000000000000,
        0b0000000000000000,
        0b0000000000000000,
        0b0000000000000000,
        0b0000000000000000,
        0b0000000000000000,
    ],
    "arrow_up": [
        0b0000000100000000,
        0b0000001110000000,
        0b0000011111000000,
        0b0000111111100000,
        0b0001111111110000,
        0b0000000100000000,
        0b0000000100000000,
        0b0000000100000000,
        0b0000000100000000,
        0b0000000100000000,
        0b0000000100000000,
        0b0000000000000000,
        0b0000000000000000,
        0b0000000000000000,
        0b0000000000000000,
        0b0000000000000000,
    ],
    "checkmark": [
        0b0000000000000000,
        0b0000000000000000,
        0b0000000000000001,
        0b0000000000000011,
        0b0000000000000110,
        0b0000000000001100,
        0b0000000000011000,
        0b0000000000110000,
        0b1000000001100000,
        0b1100000011000000,
        0b0110000110000000,
        0b0011001100000000,
        0b0001111000000000,
        0b0000110000000000,
        0b0000000000000000,
        0b0000000000000000,
    ],
    "cross": [
        0b0000000000000000,
        0b1100000000000011,
        0b0110000000000110,
        0b0011000000001100,
        0b0001100000011000,
        0b0000110000110000,
        0b0000011001100000,
        0b0000001111000000,
        0b0000001111000000,
        0b0000011001100000,
        0b0000110000110000,
        0b0001100000011000,
        0b0011000000001100,
        0b0110000000000110,
        0b1100000000000011,
        0b0000000000000000,
    ],
    "warning": [
        0b0000000100000000,
        0b0000001110000000,
        0b0000011111000000,
        0b0000111111100000,
        0b0001110110011100,
        0b0011100110001110,
        0b0111000110000111,
        0b1110000110000011,
        0b1100000110000001,
        0b1100001111000001,
        0b1100000110000001,
        0b1110000000000011,
        0b0111111111111110,
        0b0011111111111100,
        0b0000000000000000,
        0b0000000000000000,
    ],
    "music": [
        0b0000000111111110,
        0b0000001111111110,
        0b0000001100000010,
        0b0000001100000010,
        0b0000001100000010,
        0b0000001100000010,
        0b0000001100000110,
        0b0000001100001110,
        0b0000001100011110,
        0b0001111100111110,
        0b0011111101111110,
        0b0111000011111110,
        0b0110000001111110,
        0b0110000000111110,
        0b0111111100000000,
        0b0011111000000000,
    ],
}


class OLED:
    """
    NIAT Innovators Kit — OLED Display Helper
    ==========================================
    Makes the 128x64 OLED display super easy to use.
    No hardware knowledge needed — just call the functions!
    """

    def __init__(self):
        """
        Sets up the OLED display automatically.

        Example:
            screen = OLED()
        """
        try:
            i2c = busio.I2C(scl=_SCL_PIN, sda=_SDA_PIN)
            self._oled = adafruit_ssd1306.SSD1306_I2C(
                _WIDTH, _HEIGHT, i2c, addr=_I2C_ADDR
            )
        except Exception as e:
            raise RuntimeError(
                "\n[NIAT] Could not find the OLED display!\n"
                "  → Check that the display is plugged in correctly.\n"
                "  → SDA → GPIO21,  SCL → GPIO22,  VCC → 3.3V\n"
                f"  → Error: {e}\n"
            )

        self._oled.fill(0)
        self._oled.show()
        self._font_size = 1
        self._cursor_row = 1
        self._inverted = False
        print("[NIAT] OLED display ready!")

    # ── Internal helpers ──────────────────────────────────────

    def _row_to_y(self, row):
        return (row - 1) * 8 * self._font_size

    def _col_to_x(self, col):
        return (col - 1) * 6 * self._font_size

    def _max_rows(self):
        return _HEIGHT // (8 * self._font_size)

    # ── Core functions ────────────────────────────────────────

    def clear(self):
        """
        Clears everything off the screen.

        Example:
            screen.clear()
        """
        self._oled.fill(0)
        self._oled.show()
        self._cursor_row = 1

    def print(self, text, row=None, col=1):
        """
        Prints text on the screen.

        Parameters:
            text : What to display.
            row  : Which row (1 = top). Auto-advances if not given.
            col  : Which column to start at (1 = left).

        Examples:
            screen.print("Hello!")
            screen.print("Score: 10", row=2)
            screen.print("Hi", row=1, col=5)
        """
        text = str(text)

        if row is None:
            row = self._cursor_row
            self._cursor_row += 1
            if self._cursor_row > self._max_rows():
                self._cursor_row = 1

        x = self._col_to_x(col)
        y = self._row_to_y(row)

        self._oled.fill_rect(0, y, _WIDTH, 8 * self._font_size, 0)
        self._oled.text(text, x, y, 1, size=self._font_size)
        self._oled.show()

    def show_number(self, number, big=True):
        """
        Shows a number large and centered on screen.

        Parameters:
            number : The number to display.
            big    : True = large text, False = normal size.

        Examples:
            screen.show_number(42)
            screen.show_number(3.14)
        """
        self.clear()
        text = str(number)
        size = 2 if big else 1
        x = max(0, (_WIDTH - len(text) * 6 * size) // 2)
        y = (_HEIGHT - 8 * size) // 2
        self._oled.text(text, x, y, 1, size=size)
        self._oled.show()

    def show_message(self, line1="", line2="", line3="", line4=""):
        """
        Shows up to 4 lines of text at once.

        Examples:
            screen.show_message("Name: Ali", "Score: 95")
            screen.show_message("NIAT Kit", "Version 1.0")
        """
        self.clear()
        for i, line in enumerate([line1, line2, line3, line4]):
            if line:
                self._oled.text(str(line), 0, i * 16, 1, size=1)
        self._oled.show()

    # ── Icons ─────────────────────────────────────────────────

    def show_icon(self, name):
        """
        Shows a built-in icon centered on screen.

        Available: "smile", "heart", "star", "arrow_up",
                   "checkmark", "cross", "warning", "music"

        Example:
            screen.show_icon("heart")
        """
        name = name.lower().strip()
        if name not in _ICONS:
            available = ", ".join(_ICONS.keys())
            self.clear()
            self._oled.text("Unknown icon!", 0, 0, 1)
            self._oled.text(name, 0, 10, 1)
            self._oled.show()
            print(f"[NIAT] Icon '{name}' not found. Try: {available}")
            return

        self.clear()
        rows = _ICONS[name]
        x_off = (_WIDTH - 16) // 2
        y_off = (_HEIGHT - 16) // 2

        for row_idx, row_bits in enumerate(rows):
            for col_idx in range(16):
                if row_bits & (1 << (15 - col_idx)):
                    px = x_off + col_idx
                    py = y_off + row_idx
                    if 0 <= px < _WIDTH and 0 <= py < _HEIGHT:
                        self._oled.pixel(px, py, 1)
        self._oled.show()

    # ── Drawing ───────────────────────────────────────────────

    def draw_box(self, x=0, y=0, width=None, height=None):
        """
        Draws a rectangle outline on the screen.

        Examples:
            screen.draw_box()
            screen.draw_box(x=10, y=10, width=50, height=30)
        """
        w = width  if width  is not None else _WIDTH  - x
        h = height if height is not None else _HEIGHT - y
        self._oled.rect(x, y, w, h, 1)
        self._oled.show()

    def draw_line(self, direction="horizontal", position=None):
        """
        Draws a line across the screen.

        Parameters:
            direction : "horizontal" or "vertical"
            position  : Pixel position (default: center).

        Examples:
            screen.draw_line()
            screen.draw_line(direction="vertical")
        """
        d = direction.lower()
        if d in ("horizontal", "h"):
            y = position if position is not None else _HEIGHT // 2
            self._oled.hline(0, y, _WIDTH, 1)
        elif d in ("vertical", "v"):
            x = position if position is not None else _WIDTH // 2
            self._oled.vline(x, 0, _HEIGHT, 1)
        else:
            print(f"[NIAT] Use 'horizontal' or 'vertical', not '{direction}'")
            return
        self._oled.show()

    # ── Progress bar ──────────────────────────────────────────

    def progress_bar(self, value, label_text=None):
        """
        Shows a progress bar at the bottom of the screen.

        Parameters:
            value      : 0 to 100
            label_text : Optional label shown above the bar.

        Examples:
            screen.progress_bar(50)
            screen.progress_bar(75, label_text="Loading...")
        """
        value = max(0, min(100, int(value)))

        if label_text:
            self._oled.fill_rect(0, 48, _WIDTH, 8, 0)
            self._oled.text(str(label_text), 0, 48, 1)

        bar_y = 56
        self._oled.fill_rect(0, bar_y, _WIDTH, 8, 0)
        self._oled.rect(0, bar_y, _WIDTH, 8, 1)
        inner_w = int((_WIDTH - 4) * value / 100)
        if inner_w > 0:
            self._oled.fill_rect(2, bar_y + 2, inner_w, 4, 1)
        self._oled.show()

    # ── Font control ──────────────────────────────────────────

    def set_font(self, size="small"):
        """
        Changes text size for future print() calls.

        Parameters:
            size : "small" or "big"

        Examples:
            screen.set_font(size="big")
            screen.set_font(size="small")
        """
        if size in ("small", "medium"):
            self._font_size = 1
        elif size == "big":
            self._font_size = 2
        else:
            print(f"[NIAT] Font size should be 'small' or 'big', not '{size}'")

    # ── Display control ───────────────────────────────────────

    def invert(self):
        """
        Inverts screen colors (black becomes white, white becomes black).

        Example:
            screen.invert()
        """
        self._oled.invert(True)
        self._inverted = True

    def normal(self):
        """
        Returns screen to normal colors.

        Example:
            screen.normal()
        """
        self._oled.invert(False)
        self._inverted = False

    def brightness(self, level=10):
        """
        Sets screen brightness.

        Parameters:
            level : 0 (off) to 10 (brightest)

        Examples:
            screen.brightness(10)
            screen.brightness(0)
        """
        level = max(0, min(10, int(level)))
        self._oled.contrast(int(level * 25.5))

    # ── Animated helpers ──────────────────────────────────────

    def scroll_text(self, text, speed=3):
        """
        Scrolls a message across the middle of the screen.

        Parameters:
            text  : Message to scroll.
            speed : 1 (slow) to 5 (fast)

        Examples:
            screen.scroll_text("Hello NIAT!")
            screen.scroll_text("Score: 100", speed=5)
        """
        text = str(text)
        speed = max(1, min(5, int(speed)))
        delay = 0.12 / speed
        y = _HEIGHT // 2 - 4
        total_w = len(text) * 6

        for offset in range(_WIDTH + total_w):
            x = _WIDTH - offset
            self._oled.fill_rect(0, y, _WIDTH, 8, 0)
            self._oled.text(text, x, y, 1)
            self._oled.show()
            time.sleep(delay)

    def countdown(self, from_number=5, message="Go!"):
        """
        Counts down to zero then shows a final message.

        Parameters:
            from_number : Start of countdown (default 5)
            message     : Text shown at the end (default "Go!")

        Examples:
            screen.countdown()
            screen.countdown(from_number=3, message="Start!")
        """
        for n in range(int(from_number), 0, -1):
            self.show_number(n, big=True)
            time.sleep(1)
        self.clear()
        x = max(0, (_WIDTH - len(message) * 12) // 2)
        self._oled.text(message, x, _HEIGHT // 2 - 8, 1, size=2)
        self._oled.show()
        time.sleep(1)