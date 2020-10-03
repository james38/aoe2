"""
Base building class containing building properties.
"""

class Building(object):
    """docstring for Building."""

    def __init__(self, type=None):
        #super(Entity, self).__init__()
        self.hp = None
        return self

    def _is_standing(self):
        if self.hp is not None:
            if self.hp > 0:
                return True
            else:
                return False
        else:
            raise NotImplementedError
