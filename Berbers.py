"""
Class for Berbers civilization.

Cavalry and Naval civilization

• Villagers move 10% faster
• Stable units cost -15% in Castle, -20% in Imperial Age
• Ships move 10% faster

Unique Units:
Camel Archer (cavalry archer), Genitour (mounted skirmisher)

Unique Techs:
• Kasbah (team castles work 25% faster)
• Maghrebi Camels (Camel units regenerate)

Team Bonus:
Genitour available in the Archery Range starting in the Castle Age

"""
from Civ import *

class Berbers(Civilization):
    """docstring for Berbers class"""

    def __init__(self, age="Dark"):
        super().__init__()
        self.age = age

        self.unq = {
            #"Bldgs": dict(),
            "Units": {
                "Castle": [
                    "Genitour",
                    "Camel Archer"
                ],
                "Imperial": [
                    "Elite Camel Archer"
                ]
            },
            "Techs": {
                "Castle": [
                    "Kasbah"
                ],
                "Imperial": [
                    "Maghrebi Camels"
                ]
            }
        }

        self.unavail = {
            "Bldgs": [
                "Keep",
                "Bombard Tower"
            ],
            "Units": [
                "Eagle Scout",
                "Eagle Warrior",
                "Battle Elephant",
                "Steppe Lancer",
                "Arbalester",
                "Halberdier",
                "Elite Eagle Warrior",
                "Paladin",
                "Elite Battle Elephant",
                "Elite Steppe Lancer",
                "Siege Ram",
                "Siege Onager"
            ],
            "Techs": [
                "Missionary",
                "Sanctity",
                "Parthian Tactics",
                "Sappers",
                "Shipwright",
                "Architecture",
                "Bombard Tower",
                "Keep",
                "Block Printing",
                "Two-Man Saw"
            ]
        }

        self._add_unq(self.unq)
        self._remove_unavail(self.unavail)
