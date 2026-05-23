"""
NIAT Kit LED Matrix Module

Controls 4x4 WS2812B RGB LED matrix.

Current wiring:
    DIN -> GPIO18

Matrix layout:
    13   9   5   1
    14  10   6   2
    15  11   7   3
    16  12   8   4

Usage:
    from niat import PixelMatrix

    matrix = PixelMatrix()

    matrix.turn_on("red")
    matrix.turn_off()

    matrix.set_pixel(1, 2, "blue")

    matrix.show("heart")
    matrix.show("cross")
    matrix.show("diamond")
    matrix.show("arrow_up")

    matrix.blink("green")
    matrix.rainbow()
"""

import board
import neopixel
import time

_PIN = board.GPIO18
_COUNT = 16


class PixelMatrix:
    COLORS = {
        "red": (255, 0, 0),
        "green": (0, 255, 0),
        "blue": (0, 0, 255),
        "yellow": (255, 255, 0),
        "cyan": (0, 255, 255),
        "magenta": (255, 0, 255),
        "white": (255, 255, 255),
        "orange": (255, 100, 0),
        "pink": (255, 20, 100),
    }

    SYMBOLS = {
        "heart": [
            0, 1, 1, 0,
            1, 1, 1, 1,
            0, 1, 1, 0,
            0, 0, 0, 0,
        ],

        "cross": [
            1, 0, 0, 1,
            0, 1, 1, 0,
            0, 1, 1, 0,
            1, 0, 0, 1,
        ],

        "plus": [
            0, 1, 0, 0,
            1, 1, 1, 0,
            0, 1, 0, 0,
            0, 0, 0, 0,
        ],

        "diamond": [
            0, 1, 0, 0,
            1, 0, 1, 0,
            0, 1, 0, 0,
            0, 0, 0, 0,
        ],

        "square": [
            1, 1, 1, 1,
            1, 0, 0, 1,
            1, 0, 0, 1,
            1, 1, 1, 1,
        ],

        "full": [
            1, 1, 1, 1,
            1, 1, 1, 1,
            1, 1, 1, 1,
            1, 1, 1, 1,
        ],

        "center": [
            0, 0, 0, 0,
            0, 1, 1, 0,
            0, 1, 1, 0,
            0, 0, 0, 0,
        ],

        "corners": [
            1, 0, 0, 1,
            0, 0, 0, 0,
            0, 0, 0, 0,
            1, 0, 0, 1,
        ],

        "checker": [
            1, 0, 1, 0,
            0, 1, 0, 1,
            1, 0, 1, 0,
            0, 1, 0, 1,
        ],

        "diagonal_left": [
            1, 0, 0, 0,
            0, 1, 0, 0,
            0, 0, 1, 0,
            0, 0, 0, 1,
        ],

        "diagonal_right": [
            0, 0, 0, 1,
            0, 0, 1, 0,
            0, 1, 0, 0,
            1, 0, 0, 0,
        ],

        "arrow_up": [
            0, 1, 0, 0,
            1, 1, 1, 0,
            0, 1, 0, 0,
            0, 1, 0, 0,
        ],

        "arrow_down": [
            0, 1, 0, 0,
            0, 1, 0, 0,
            1, 1, 1, 0,
            0, 1, 0, 0,
        ],

        "arrow_left": [
            0, 1, 0, 0,
            1, 1, 0, 0,
            1, 1, 0, 0,
            0, 1, 0, 0,
        ],

        "arrow_right": [
            0, 1, 0, 0,
            0, 1, 1, 0,
            0, 1, 1, 0,
            0, 1, 0, 0,
        ],

        "triangle_up": [
            0, 1, 0, 0,
            1, 1, 1, 0,
            1, 0, 0, 1,
            0, 0, 0, 0,
        ],

        "triangle_down": [
            1, 0, 0, 1,
            1, 1, 1, 0,
            0, 1, 0, 0,
            0, 0, 0, 0,
        ],

        "wave": [
            1, 0, 0, 1,
            0, 1, 1, 0,
            1, 0, 0, 1,
            0, 1, 1, 0,
        ],

        "bars": [
            1, 0, 1, 0,
            1, 0, 1, 0,
            1, 0, 1, 0,
            1, 0, 1, 0,
        ],
    }

    def __init__(self, brightness=0.2):
        try:
            self.matrix = neopixel.NeoPixel(
                _PIN,
                _COUNT,
                brightness=brightness,
                auto_write=False
            )
            self.turn_off()
        except Exception:
            raise RuntimeError(
                "PixelMatrix not found. Is the LED matrix plugged in?"
            )

    def _color(self, color):
        return self.COLORS.get(color.lower(), (255, 255, 255))

    def _xy_to_index(self, x, y):
        mapping = [
            [12, 8, 4, 0],
            [13, 9, 5, 1],
            [14, 10, 6, 2],
            [15, 11, 7, 3],
        ]
        return mapping[y][x]

    def turn_off(self):
        self.matrix.fill((0, 0, 0))
        self.matrix.show()

    def turn_on(self, color="white"):
        self.matrix.fill(self._color(color))
        self.matrix.show()

    def set_pixel(self, x, y, color="white"):
        index = self._xy_to_index(x, y)
        self.matrix[index] = self._color(color)
        self.matrix.show()

    def show(self, symbol, color="red"):
        if symbol not in self.SYMBOLS:
            raise ValueError("Symbol not available.")

        self.turn_off()
        pattern = self.SYMBOLS[symbol]
        rgb = self._color(color)

        for y in range(4):
            for x in range(4):
                if pattern[y * 4 + x]:
                    index = self._xy_to_index(x, y)
                    self.matrix[index] = rgb

        self.matrix.show()

    def blink(self, color="white", times=3, delay=0.3):
        rgb = self._color(color)

        for _ in range(times):
            self.matrix.fill(rgb)
            self.matrix.show()
            time.sleep(delay)

            self.turn_off()
            time.sleep(delay)

    def rainbow(self, delay=0.05):
        for shift in range(255):
            for i in range(_COUNT):
                self.matrix[i] = (
                    (i * 5 + shift) % 255,
                    (i * 10 + shift) % 255,
                    (i * 15 + shift) % 255
                )
            self.matrix.show()
            time.sleep(delay)
    def demo(self, delay=1.5):
        symbols = [
            "heart",
            "cross",
            "plus",
            "diamond",
            "square",
            "full",
            "center",
            "corners",
            "checker",
            "diagonal_left",
            "diagonal_right",
            "arrow_up",
            "arrow_down",
            "arrow_left",
            "arrow_right",
            "triangle_up",
            "triangle_down",
            "wave",
            "bars",
        ]

        colors = [
            "red",
            "green",
            "blue",
            "yellow",
            "cyan",
            "magenta",
            "white",
            "orange",
            "pink",
        ]

        while True:
            for symbol in symbols:
                for color in colors:
                    self.show(symbol, color)
                    time.sleep(delay)