# --- Imports --- #

from dataclasses import dataclass
from typing import Self

from .appearance.body import Body
from .names import Name


# --- Person Class --- #

@dataclass(slots = True)
class Person:
    name: Name
    body: Body
    
    def give_name(self, first: str, middle: str = "") -> Name:
        return Name(first, self.name.last, middle)
        
    def change_name(self, name: Name):
        
        if name.last != self.name.last:
            return
        
        self.name = name
        
    def marry(self, person: Self):
        self.name.last = person.name.last
        
    def __str__(self) -> str:
        return str(self.name)
        
    def __format__(self, format_spec="%d") -> str:
        """Returns a formatted string,
        %d = Description,
        %f = Full name"""
        
        if format_spec.strip() == "%f":
                return f"{self.name: %f}"
        return str(self)