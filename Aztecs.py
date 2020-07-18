"""
Class for Aztec civilization.

Infantry and Monk civilization

- Villagers carry +5
- Military units created 10% faster
- +5 Monk hit points for each Monastery technology
- Start with +50 gold

Unique Unit:
Jaguar Warrier (infantry)

Unique Techs:
- Atlatl (Skirmishers +1 attack, +1 range)
- Garland Wars (+4 infantry attack)

Team Bonus:
Relics generate +33% gold
"""
from Civ import *

class Aztecs(Civilization):
    """docstring for Aztecs class"""

    def __init__(self, age="Dark"):
        super().__init__()
        self.age = age

        self.unq = {
            #"Bldgs": dict(),
            "Units": {
                "Castle": [
                    "Jaguar Warrior"
                ],
                "Imperial": [
                    "Elite Jaguar"
                ]
            },
            "Techs": {
                "Castle": [
                    "Atlatl"
                ],
                "Imperial": [
                    "Garland Wars"
                ]
            }
        }

        self.unavail = {
            "Bldgs": [
                "Stable",
                "Keep",
                "Bombard Tower"
            ],
            "Units": [
                "Scout Cavalry",
                "Cavalry Archer",
                "Light Cavalry",
                "Knight",
                "Camel Rider",
                "Battle Elephant",
                "Steppe Lancer",
                "Hand Cannoneer",
                "Heavy Cav Archer",
                "Halberdier",
                "Hussar",
                "Cavalier",
                "Paladin",
                "Heavy Camel Rider",
                "Elite Battle Elephant",
                "Elite Steppe Lancer",
                "Heavy Scorpion",
                "Bombard Cannon",
                "Cannon Galleon",
                "Elite Cannon Galleon",
                "Heavy Demo Ship",
                "Galleon"
            ],
            "Techs": [
                "Bloodlines",
                "Scale Barding Armor",
                "Thumb Ring",
                "Husbandry",
                "Chain Barding Armor",
                "Masonry",
                "Parthian Tactics",
                "Ring Archer Armor",
                "Plate Barding Armor",
                "Architecture",
                "Bombard Tower",
                "Keep",
                "Hoardings",
                "Two-Man Saw",
                "Guilds"
            ]
        }

        self._add_unq(self.unq)
        self._remove_unavail(self.unavail)
