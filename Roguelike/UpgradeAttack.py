from Inventory import *

import random as rnd


class UpgradeAttack(Inventory):
    def __init__(self):
        super().__init__()
        rnd.seed()
        self.symbol = '('
        self.array_symbol = b'('
        self.attack = rnd.normalvariate(2, 0.5)
        self.health = 0
        self.name = "Attack updater (w/s)"
