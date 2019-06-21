from RogueConstants import start_health, start_attack
from MapObjects.Character.Character import *


class Player(Character):
    def __init__(self):
        super().__init__()
        self.symbol = '@'
        self.array_symbol = b'@'
        self.health = start_health * 2
        self.attack = start_attack * 2
        self.wins_on_level = 0
        self.level = 0

    def get_desired_position(self, map_cells, direction):
        if direction == "up" and self.y > 0 and map_cells[self.y - 1][self.x].free_to_move:
            return self.x, self.y - 1
        if direction == "down" and self.y < len(map_cells) - 1 and map_cells[self.y + 1][self.x].free_to_move:
            return self.x, self.y + 1
        if direction == "right" and self.x < len(map_cells[0]) - 1 and map_cells[self.y][self.x + 1].free_to_move:
            return self.x + 1, self.y
        if direction == "left" and self.x > 0 and map_cells[self.y][self.x - 1].free_to_move:
            return self.x - 1, self.y
        return self.x, self.y

    def upgrade_level(self):
        self.level += 1
        self.health *= 1.1
        self.attack *= 1.1
