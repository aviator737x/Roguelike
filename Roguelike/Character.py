from RogueConstants import start_health, start_attack
from MapObject import *


class Character(MapObject):
    def __init__(self):
        super().__init__()
        self.health = start_health
        self.attack = start_attack
        self.backpack = dict()
        self.worn = dict()

    # TODO: implement battle
    # None if nobody wins
    @staticmethod
    def battle(players):
        lossers = set()
        players = list(players)
        for player1 in range(len(players)):
            for player2 in range(len(players)):
                if player1 != player2:
                    players[player1].health -= players[player2].attack
                    players[player2].health -= players[player1].attack
            if players[player1].health <= 0:
                lossers.add(players[player1])
        if lossers:
            return lossers
        return None

    def add_to_backpack(self, inventory):
        inventory_name = inventory.name
        if inventory_name in self.backpack:
            self.backpack[inventory_name].append(inventory)
        else:
            self.backpack[inventory_name] = [inventory]

    def wear_from_backpack(self, inventory_name):
        if inventory_name in self.backpack:
            if self.backpack[inventory_name]:
                inventory = self.backpack[inventory_name].pop()
                self.attack += inventory.attack
                self.health += inventory.health
                if inventory_name in self.worn:
                    self.worn[inventory_name].append(inventory)
                else:
                    self.worn[inventory_name] = [inventory]

    def take_of(self, inventory_name):
        if inventory_name in self.worn:
            inventory = self.worn[inventory_name].pop()
            self.attack -= inventory.attack
            self.health -= inventory.health
            if inventory_name in self.backpack:
                self.backpack[inventory_name].append(inventory)
            else:
                self.backpack[inventory_name] = [inventory]