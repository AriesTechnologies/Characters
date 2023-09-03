# --- Imports --- #

from dataclasses import dataclass, field
from enum import IntEnum, auto


# --- Color Enum --- #

class Color(IntEnum):
    BROWN = auto()
    BLONDE = auto()
    BLACK = auto()
    RED = auto()
    GREY = auto()
    

# --- Style Enum --- #

class Style(IntEnum):
    STRAIGHT = auto()
    WAVY = auto()
    CURLY = auto()
    

# --- Thickness Enum --- #

class Thickness(IntEnum):
    BALD = auto()
    BALDING = auto()
    SHORT = auto()
    MEDIUM = auto()
    LONG = auto()
    
    
# --- Hair Class --- #

@dataclass(slots = True)
class Hair:
    color: Color = field(default=Color.BROWN)
    style: Style = field(default=Style.STRAIGHT)
    thickness: Thickness = field(default=Thickness.MEDIUM)
    
    def __str__(self):
        return f"{self.color.name}, {self.style.name}, {self.thickness.name} hair"
        
    # def __format__(self, format_spec="%d") -> str:
    #     """Returns a formatted string,
    #     %d = Description"""
        
    #     return str(self)
