# --- Imports --- #

from dataclasses import dataclass, field
from enum import IntEnum, auto


# --- Tone Enum --- #

class Tone(IntEnum):
    WHITE = auto()
    BROWN = auto()
    BLACK = auto()
    

# --- Freckled Enum --- #

class Freckled(IntEnum):
    NONE = auto()
    FRECKLED = auto()
    

# --- Abnormalities Enum --- #

class Abnormalities(IntEnum):
    NONE = auto()
    DISCOLORATION = auto()
    
    
# --- Skin Class --- #

@dataclass(slots = True)
class Skin:
    tone: Tone
    freckles: Freckled = field(default=Freckled.NONE)
    abnormalities: Abnormalities = field(default=Abnormalities.NONE)
    
    def __str__(self):
        return f"{self.tone} skin"