"""
NIAT Kit Microphone Module

Uses SPH0645LM4H-B I2S MEMS microphone.

Current wiring:
    BCLK -> GPIO38
    WS   -> GPIO39
    DATA -> GPIO40

Usage:
    from niat import MicSensor

    mic = MicSensor()

    print(mic.read_percent())
    print(mic.read_level())
    print(mic.is_loud())

    mic.monitor()
"""

import board
import audiobusio
import array
import math
import time

_BCLK = board.GPIO38
_WS = board.GPIO39
_DATA = board.GPIO40
_BUFFER_SIZE = 256


class MicSensor:
    def __init__(self):
        try:
            self.mic = audiobusio.I2SIn(
                bit_clock=_BCLK,
                word_select=_WS,
                data=_DATA
            )

            self.buffer = array.array("h", [0] * _BUFFER_SIZE)

        except Exception as e:
            raise RuntimeError(
                f"MicSensor not found: {e}"
            )

    def _read_amplitude(self):
        self.mic.record(self.buffer, len(self.buffer))

        peak = 0

        for sample in self.buffer:
            level = abs(sample)
            if level > peak:
                peak = level

        return peak

    def read_percent(self):
        amplitude = self._read_amplitude()

        percent = int((amplitude / 30000) * 100)

        if percent > 100:
            percent = 100

        if percent < 0:
            percent = 0

        return percent

    def read_level(self):
        percent = self.read_percent()

        if percent < 10:
            return "silent"
        elif percent < 25:
            return "quiet"
        elif percent < 50:
            return "normal"
        elif percent < 75:
            return "loud"
        else:
            return "very loud"

    def is_loud(self, threshold=60):
        return self.read_percent() >= threshold

    def monitor(self, delay=0.5):
        while True:
            print(
                "Sound:",
                self.read_percent(),
                "%",
                "|",
                self.read_level()
            )
            time.sleep(delay)