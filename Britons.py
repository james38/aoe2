"""
Class for Briton civilization.

Foot Archer civilization

• Town Centers cost -50% wood in Castle Age
• Foot archers (except skirmishers) have +1 range Castle Age, +1 range Imperial Age (for +2 total)
• Shepherds work 25% faster

Unique Unit:
Longbowman (archer)

Unique Techs:
• Yeomen (+1 foot archer range, +2 tower attack)
• Warwolf (Trebuchets do blast damage)

Team Bonus:
Archery Ranges work 20% faster
"""
from Civ import *

class Britons(Civilization):
    """docstring for Britons class"""

    def __init__(self, age="Dark"):
        super().__init__()
        self.age = age

        self.unq = {
            #"Bldgs": dict(),
            "Units": {
                "Castle": [
                    "Longbowman"
                ],
                "Imperial": [
                    "Elite Longbowman"
                ]
            },
            "Techs": {
                "Castle": [
                    "Yeomen"
                ],
                "Imperial": [
                    "Warwolf"
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
                "Battle Elephant",
                "Steppe Lancer",
                "Hand Cannoneer",
                "Elite Eagle Warrior",
                "Hussar",
                "Paladin",
                "Heavy Camel Rider",
                "Elite Battle Elephant",
                "Elite Steppe Lancer",
                "Siege Ram",
                "Siege Onager",
                "Bombard Cannon",
                "Elite Cannon Galleon"
            ],
            "Techs": [
                "Bloodlines",
                "Thumb Ring",
                "Treadmill Crane",
                "Missionary",
                "Redemption",
                "Atonement",
                "Heresy",
                "Stone Shaft Mining",
                "Parthian Tactics",
                "Bombard Tower",
                "Crop Rotation"
            ]
        }

        self._add_unq(self.unq)
        self._remove_unavail(self.unavail)
