from Inventory import *


class UpgradeBoth(Inventory):
    def __init__(self):
        super().__init__()
        self.symbol = '?'
        self.array_symbol = b'?'
        self.health = rnd.normalvariate(2, 0.5)
        self.attack = rnd.normalvariate(1, 0.25)
        self.name = "A/H upgrader (r/f)"

