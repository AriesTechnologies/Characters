# --- Imports --- #

from dataclasses import dataclass, field
from enum import IntEnum, auto

from .skin import Skin
from .head.head import Head


# --- Sex Enum --- #

class Sex(IntEnum):
    MALE = auto()
    FEMALE = auto()
    

Gender = Sex


# --- BloodType Enum --- #

class BloodType(IntEnum):
    O_POS = auto()
    O_NEG = auto()
    A_POS = auto()
    A_NEG = auto()
    B_POS = auto()
    B_NEG = auto()
    AB_POS = auto()
    AB_NEG = auto()
    
    
# --- BMICategory Enum --- #

class BMICategory(IntEnum):
    UNDERWEIGHT = auto()
    NORMAL = auto()
    OVERWEIGHT = auto()
    OBESE = auto()
    
    
# --- Body Class --- #

@dataclass(slots = True)
class Body:
    sex: Sex
    skin: Skin
    head: Head
    bmi: BMICategory = field(default=BMICategory.NORMAL)
    bloodType: BloodType = field(default=BloodType.O_POS)
    
    def __str__(self):
        gendered_noun = "He" if self.sex == Sex.MALE else "She"
        return f"{gendered_noun} is {self.sex}, who is {self.bmi}, with {self.skin}, with {self.head}"