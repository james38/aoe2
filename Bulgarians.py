"""
Class for Bulgarians civilization.

Infantry and Cavalry civilization

• Militia-line upgrades free
• Town Centers cost -50% stone
• Can build Krepost

Unique Unit:
Konnik (cavalry)

Unique Techs:
• Stirrups (Cavalry attack 25% faster)
• Bagains (Militia-line gains +5 armor)

Team Bonus:
Blacksmiths work 50% faster

"""
from Civ import *

class Bulgarians(Civilization):
    """docstring for Bulgarians class"""

    def __init__(self, age="Dark"):
        super().__init__()
        self.age = age

        self.unq = {
            "Bldgs": {
                "Castle": [
                    "Krepost"
                ]
            },
            "Units": {
                "Castle": [
                    "Konnik"
                ],
                "Imperial": [
                    "Elite Konnik"
                ]
            },
            "Techs": {
                "Castle": [
                    "Stirrups"
                ],
                "Imperial": [
                    "Bagains"
                ]
            }
        }

        self.unavail = {
            "Bldgs": [
                "Fortified Wall",
                "Bombard Tower"
            ],
            "Units": [
                "Eagle Scout",
                "Crossbowman",
                "Eagle Warrior",
                "Camel Rider",
                "Battle Elephant",
                "Steppe Lancer",
                "Arbalester",
                "Hand Cannoneer",
                "Elite Eagle Warrior",
                "Heavy Camel Rider",
                "Elite Battle Elephant",
                "Elite Steppe Lancer",
                "Paladin",
                "Bombard Cannon",
                "Fast Fire Ship",
                "Elite Cannon Galleon",
                "Heavy Demolition Ship"
            ],
            "Techs": [
                "Fortified Wall",
                "Treadmill Crane",
                "Missionary",
                "Atonement",
                "Sanctity",
                "Ring Archer Armor",
                "Dry Dock",
                "Shipwright",
                "Bombard Tower",
                "Arrowslits",
                "Hoardings",
                "Sappers",
                "Faith",
                "Block Printing",
                "Two-Man Saw",
                "Guilds"
            ]
        }

        self._add_unq(self.unq)
        self._remove_unavail(self.unavail)
