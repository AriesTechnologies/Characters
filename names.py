# --- Imports --- #

from dataclasses import dataclass, field


# --- Name Class --- #

@dataclass(slots = True)
class Name:
    first: str
    last: str = field(default="")
    middle: str = field(default="")
    nickname: str = field(default="")
    
    def __post_init__(self):
        
        if self.first == "":
            raise ValueError("Invalid value for a first name.")
    
    @property
    def initials(self) -> str:
        return f"{self.first[0]}{self.middle_inital}{self.last_initial}"
        
    @property
    def middle_inital(self) -> str:
        
        if self.middle == "":
            return self.middle
        
        return self.middle[0]
        
    @property
    def last_inital(self) -> str:
        
        if self.last == "":
            return self.last
        
        return self.last[0]
        
    def __str__(self):
        return self.first
        
    def __format__(self, format_spec="%f") -> str:
        """Returns a formatted string,
        %f = Full name"""
        
        return f"{self.first} {self.middle} {self.last}"
