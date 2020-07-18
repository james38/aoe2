"""
Base civilization class containing civilization methods.
"""

class Civilization(object):
    """docstring for Entity."""

    def __init__(self, age="Dark"):
        #super(Entity, self).__init__()
        self.ages = (
            "Dark",
            "Feudal",
            "Castle",
            "Imperial"
        )

        self._set_age(age)

        self.bldgs = {
            "Dark": [
                "Barracks",
                "Dock",
                "Outpost",
                "Palisade Wall",
                "Palisade Gate",
                "House",
                "Town Center",
                "Mining Camp",
                "Lumber Camp",
                "Mill",
                "Farm"
            ],
            "Feudal": [
                "Archery Range",
                "Stable",
                "Blacksmith",
                "Fish Trap",
                "Watch Tower",
                "Gate",
                "Stone Wall",
                "Market"
            ],
            "Castle": [
                "Siege Workshop",
                "University",
                "Guard Tower",
                "Fortified Wall",
                "Castle",
                "Monastery",
                "Town Center"
            ],
            "Imperial": [
                "Keep",
                "Bombard Tower",
                "Wonder"
            ]
        }

        self.units = {
            "Dark": [
                "Militia",
                "Fishing Ship",
                "Transport Ship",
                "Villager"
            ],
            "Feudal": [
                "Archer",
                "Skirmisher",
                "Man-at-Arms",
                "Spearman",
                "Eagle Scout",
                "Scout Cavalry",
                "Fire Galley",
                "Trade Cog",
                "Demolition Raft",
                "Galley",
                "Trade Cart"
            ],
            "Castle": [
                "Crossbowman",
                "Elite Skirmisher",
                "Cavalry Archer",
                "Long Swordsman",
                "Pikeman",
                "Eagle Warrior",
                "Light Cavalry",
                "Knight",
                "Camel Rider",
                "Battle Elephant",
                "Steppe Lancer",
                "Battering Ram",
                "Mangonel",
                "Scorpion",
                "Siege Tower",
                "Fire Ship",
                "Demolition Ship",
                "War Galley",
                "Petard",
                "Monk"
            ],
            "Imperial": [
                "Arbalester",
                "Hand Cannoneer",
                "Heavy Cav Archer",
                "Two-Handed Swordsman",
                "Champion",
                "Halberdier",
                "Elite Eagle Warrior",
                "Hussar",
                "Cavalier",
                "Paladin",
                "Heavy Camel Rider",
                "Elite Battle Elephant",
                "Elite Steppe Lancer",
                "Capped Ram",
                "Siege Ram",
                "Onager",
                "Siege Onager",
                "Heavy Scorpion",
                "Bombard Cannon",
                "Fast Fire Ship",
                "Cannon Galleon",
                "Elite Cannon Galleon",
                "Heavy Demo Ship",
                "Galleon",
                "Trebuchet"
            ]
        }

        self.techs = {
            "Dark": [
                "Loom",
                "Feudal Age"
            ],
            "Feudal": [
                "Supplies",
                "Bloodlines",
                "Padded Archer Armor",
                "Fletching",
                "Forging",
                "Scale Barding Armor",
                "Scale Mail Armor",
                "Town Watch",
                "Castle Age",
                "Wheelbarrow",
                "Gold Mining",
                "Stone Mining",
                "Double-Bit Axe",
                "Horse Collar"
            ],
            "Castle": [
                "Thumb Ring",
                "Squires",
                "Arson",
                "Husbandry",
                "Leather Archer Armor",
                "Bodkin Arrow",
                "Iron Casting",
                "Chain Barding Armor",
                "Chain Mail Armor",
                "Gillnets",
                "Careening",
                "Masonry",
                "Fortified Wall",
                "Ballistics",
                "Guard Tower",
                "Heated Shot",
                "Murder Holes",
                "Treadmill Crane",
                "Redemption",
                "Atonement",
                "Herbal Medicine",
                "Heresy",
                "Sanctity",
                "Fervor",
                "Town Patrol",
                "Imperial Age",
                "Hand Cart",
                "Gold Shaft Mining",
                "Stone Shaft Mining",
                "Bow Saw",
                "Coinage",
                "Caravan",
                "Heavy Plow"
            ],
            "Imperial": [
                "Parthian Tactics",
                "Ring Archer Armor",
                "Bracer",
                "Blast Furnace",
                "Plate Barding Armor",
                "Plate Mail Armor",
                "Dry Dock",
                "Shipwright",
                "Architecture",
                "Chemistry",
                "Bombard Tower",
                "Siege Engineers",
                "Keep",
                "Arrowslits",
                "Hoardings",
                "Sappers",
                "Conscription",
                "Spies",
                "Faith",
                "Illumination",
                "Block Printing",
                "Theocracy",
                "Two-Man Saw",
                "Banking",
                "Guilds",
                "Crop Rotation"
            ]
        }

    def _set_age(self, age):
        if age in self.ages:
            self.age = age
        else:
            raise AgeError
        return self

    def _advance_age(self):
        if self.age == "Dark":
            self.age = "Feudal"
        elif self.age == "Feudal":
            self.age = "Castle"
        elif self.age == "Castle":
            self.age = "Imperial"
        else:
            raise exception
        return self

    def ent_str_to_obj(self, ent_str):
        if ent_str == "Bldgs":
            entity = self.bldgs
        elif ent_str == "Units":
            entity = self.units
        elif ent_str == "Techs":
            entity = self.techs
        return entity

    def _remove_unavail(self, ents_unavails):
        for ent_type, unavails in ents_unavails.items():
            entity = self.ent_str_to_obj(ent_type)
            for unavail in unavails:
                for age,ents in entity.items():
                    if unavail in ents:
                        ents.remove(unavail)
        return self

    def _add_unq(self, ents_ages_unqs):
        for ent_type, ages_unqs in ents_ages_unqs.items():
            entity = self.ent_str_to_obj(ent_type)
            for age, unqs in ages_unqs.items():
                for unq in unqs:
                    entity[age].append(unq)
        return self
