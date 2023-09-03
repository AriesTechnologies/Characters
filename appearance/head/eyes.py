# --- Imports --- #

from dataclasses import dataclass, field
from enum import IntEnum, auto
from typing import Optional, Self


# --- Color Enum --- #

class Color(IntEnum):
    BROWN = auto()
    BLUE = auto()
    GREEN = auto()
    HAZEL = auto()
    

# --- Shape Enum --- #

class Shape(IntEnum):
    ROUND = auto()
    ALMOND = auto()
    
    
@dataclass(slots = True)
class Eyes:
    color: Optional[Color] = field(default=Color.BROWN)
    shape: Optional[Shape] = field(default=Shape.ALMOND)
    
    def __str__(self):
        return f"{self.color.name}, {self.shape.name}-shaped eyes"