from MapObject import *
import random as rnd


class Inventory(MapObject):
    def __init__(self):
        super().__init__()
        rnd.seed()
        self.is_character = False
        self.name = " "
