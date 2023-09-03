# --- Imports --- #

import appearance.head.hair as hair
import appearance.head.eyes as eyes
import appearance.head.head as head
import appearance.body as body
import appearance.skin as skin

import names, persons


# --- Vars --- #

head1 = head.Head(hair.Hair(hair.Color.RED, hair.Style.CURLY, hair.Thickness.SHORT),
    eyes.Eyes(eyes.Color.BLUE))
person1 = persons.Person(names.Name("AtlasDisease", "B", "K"),
    body.Body(body.Sex.MALE, skin.Tone.WHITE, head1, body.BMICategory.OVERWEIGHT))

print(f"{person1: %f}")