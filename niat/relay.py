"""
NIAT Kit Relay Module
Controls 2-channel relay switches for high-power devices.

Usage:
    from niat import Switch
    
    relay = Switch(channel=1)
    
    # Turn relay on
    relay.on()
    
    # Turn relay off
    relay.off()
    
    # Check status
    if relay.is_on():
        print("Relay is on!")
    
    # Toggle state
    relay.toggle()
"""

import board
import digitalio


# Pin configuration
_CH1_PIN = board.GPIO16  # Channel 1
_CH2_PIN = board.GPIO18  # Channel 2


class Switch:
    """
    A class to control relay switches.
    
    Supports 2 independent channels for controlling high-power devices.
    Note: Relays are active-LOW (False = ON, True = OFF)
    """
    
    def __init__(self, channel=1):
        """
        Initialize the relay switch.
        
        Args:
            channel: Relay channel (1 or 2)
        """
        if channel not in [1, 2]:
            raise ValueError("Channel must be 1 or 2")
        
        self.channel = channel
        pin = _CH1_PIN if channel == 1 else _CH2_PIN
        
        try:
            self._relay = digitalio.DigitalInOut(pin)
            self._relay.direction = digitalio.Direction.OUTPUT
            self._relay.value = True  # Start off (inverted logic)
        except Exception:
            raise RuntimeError(
                f"Relay channel {channel} not found. Is the relay module plugged in?"
            )
    
    def on(self):
        """
        Turn the relay on.
        """
        self._relay.value = False
    
    def off(self):
        """
        Turn the relay off.
        """
        self._relay.value = True
    
    def is_on(self):
        """
        Check if the relay is currently on.
        
        Returns:
            bool: True if relay is on, False if off
        """
        return not self._relay.value
    
    def toggle(self):
        """
        Toggle the relay state (on becomes off, off becomes on).
        """
        self._relay.value = not self._relay.value