# --- Imports --- #

from .appearance.head import hair, eyes, head
from .appearance import body
from .appearance import skin
from .names import Name
from .persons import Person


# --- Vars --- #

# head1 = head.Head(hair.Hair(hair.Color.RED, hair.Style.CURLY, hair.Thickness.SHORT),
#     eyes.Eyes(eyes.Color.BLUE))
# person1 = Person(Name("AtlasDisease", "B", "K"),
#     body.Body(body.Sex.MALE, skin.Tone.WHITE, head1, body.BMICategory.OVERWEIGHT))

# print(f"{person1: %f}")