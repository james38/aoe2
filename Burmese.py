"""
Class for Burmese civilization.

Monk and Elephant civilization

• Lumber Camp upgrades free
• Infantry +1 attack per age (starting in the Feudal Age)
• Monastery techs cost -50%

Unique Unit:
Arambai (ranged cavalry)

Unique Techs:
• Howdah (Battle Elephants +1/+1P armor)
• Manipur Cavalry (Cavalry and Arambai +6 attack vs. buildings)

Team Bonus:
Relics visible on the map at the start of the game
"""
from Civ import *

class Burmese(Civilization):
    """docstring for Burmese class"""

    def __init__(self, age="Dark"):
        super().__init__()
        self.age = age

        self.unq = {
            #"Bldgs": dict(),
            "Units": {
                "Castle": [
                    "Arambai"
                ],
                "Imperial": [
                    "Elite Arambai"
                ]
            },
            "Techs": {
                "Castle": [
                    "Howdah"
                ],
                "Imperial": [
                    "Manipur Cavalry"
                ]
            }
        }

        self.unavail = {
            "Bldgs": [
                "Bombard Tower"
            ],
            "Units": [
                "Eagle Scout",
                "Eagle Warrior",
                "Camel Rider",
                "Steppe Lancer",
                "Arbalester",
                "Hand Cannoneer",
                "Elite Eagle Warrior",
                "Paladin",
                "Heavy Camel Rider",
                "Elite Steppe Lancer",
                "Siege Ram",
                "Siege Onager",
                "Fast Fire Ship",
                "Heavy Demolition Ship"
            ],
            "Techs": [
                "Thumb Ring",
                "Leather Archer Armor",
                "Missionary",
                "Heresy",
                "Stone Shaft Mining",
                "Ring Archer Armor",
                "Shipwright",
                "Arrowslits",
                "Bombard Tower",
                "Hoardings",
                "Sappers"
            ]
        }

        self._add_unq(self.unq)
        self._remove_unavail(self.unavail)
