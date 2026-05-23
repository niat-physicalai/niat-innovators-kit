"""
NIAT Kit Buzzer Module
Controls piezo buzzer for tones and alerts.

Usage:
    from niat import Melody
    
    buzzer = Melody()
    
    # Play a beep
    buzzer.beep()
    
    # Play a note (frequency in Hz)
    buzzer.play_tone(frequency=440, duration=0.5)
    
    # Play a melody
    buzzer.play_melody([440, 494, 523], duration=0.3)
    
    # Alert sound
    buzzer.alert()
"""

import board
import pwmio
import time


# Pin configuration
_BUZZER_PIN = board.GPIO46

# Frequencies for notes
NOTES = {
    "C4": 262,
    "D4": 294,
    "E4": 330,
    "F4": 349,
    "G4": 392,
    "A4": 440,
    "B4": 494,
    "C5": 523,
    "D5": 587,
    "E5": 659,
    "F5": 698,
    "G5": 784,
    "A5": 880,
    "B5": 988,
    "C6": 1047,
}


class Melody:
    """
    A class to control the piezo buzzer.
    
    Plays tones, melodies, and alert sounds.
    """
    
    def __init__(self):
        """
        Initialize the buzzer.
        """
        try:
            self._buzzer = pwmio.PWMOut(_BUZZER_PIN, variable_frequency=True)
            self._buzzer.frequency = 1000
            self._buzzer.duty_cycle = 0  # Start silent
        except Exception:
            raise RuntimeError(
                "Buzzer not found. Is the buzzer connected?"
            )
    
    def play_tone(self, frequency=440, duration=0.5):
        """
        Play a single tone.
        
        Args:
            frequency: Frequency in Hz (e.g., 440 for A4)
            duration: Duration in seconds
        """
        self._buzzer.frequency = frequency
        self._buzzer.duty_cycle = 32768  # 50% volume
        time.sleep(duration)
        self._buzzer.duty_cycle = 0  # Stop
    
    def play_note(self, note, duration=0.5):
        """
        Play a musical note by name.
        
        Args:
            note: Note name (e.g., "A4", "C5")
            duration: Duration in seconds
        """
        if note not in NOTES:
            raise ValueError(f"Unknown note: {note}")
        frequency = NOTES[note]
        self.play_tone(frequency, duration)
    
    def play_melody(self, frequencies, duration=0.3):
        """
        Play a sequence of tones.
        
        Args:
            frequencies: List of frequencies or note names
            duration: Duration for each tone
        """
        for freq in frequencies:
            if isinstance(freq, str):
                self.play_note(freq, duration)
            else:
                self.play_tone(freq, duration)
            time.sleep(0.1)  # Gap between notes
    
    def beep(self, count=1, duration=0.1):
        """
        Play a beep sound.
        
        Args:
            count: Number of beeps
            duration: Duration of each beep
        """
        for _ in range(count):
            self.play_tone(frequency=1000, duration=duration)
            time.sleep(0.1)
    
    def alert(self, duration=2.0):
        """
        Play an alert sound.
        
        Args:
            duration: Total duration of alert
        """
        end_time = time.monotonic() + duration
        while time.monotonic() < end_time:
            self.play_tone(frequency=800, duration=0.1)
            self.play_tone(frequency=1200, duration=0.1)