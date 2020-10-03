"""
Villager class
"""

class Villager(Unit):
    """docstring for Villager class"""

    def __init__(self):
        super().__init__()
        self.wood = 0.388 # wood/sec
        self.berries = 0.310
        self.gold = 0.379
        self.stone = 0.359
        self.fish = 0.426
        self.sheep = 0.330
        self.hunt = 0.408
        self.farm = 0.319

        self.carry = 10
        self.speed = 0.8

        self.hp = 40
        self.attack = 3
        self.melee_armor = 1
        self.pierce_armor = 1

        return self
