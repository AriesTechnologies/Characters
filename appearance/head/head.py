# --- Imports --- #

from dataclasses import dataclass, field
from enum import IntEnum, auto

from .hair import Hair
from .eyes import Eyes


# --- Shape Enum --- #

class Shape(IntEnum):
    ROUND = auto()
    

# --- Head Class --- #

@dataclass(slots = True)
class Head:
    hair: Hair = field(default=Hair)
    eyes: Eyes = field(default=Eyes)
    shape: Shape = field(default=Shape.ROUND)
    
    def __str__(self):
        return f"{self.hair}, and {self.eyes}"