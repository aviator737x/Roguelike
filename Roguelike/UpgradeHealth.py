from Inventory import *


class UpgradeHealth(Inventory):
    def __init__(self):
        super().__init__()
        self.symbol = ')'
        self.array_symbol = b')'
        self.health = rnd.normalvariate(4, 1)
        self.attack = 0
        self.name = "Health upgrader (e/d)"
