import random as rnd

from Player import *


class ConfusionDecorator(Player):
    def __init__(self, player, duration):
        rnd.seed()
        super().__init__()
        self.player = player
        self.duration = duration
        self.x = player.x
        self.y = player.y

    def set_position(self, x, y):
        super().set_position(x, y)
        self.player.set_position(x, y)

    def get_desired_position(self, game_map, key):
        new_x, new_y = self.player.get_desired_position(game_map, key)
        if self.duration == 0:
            return new_x, new_y
        self.duration -= 1
        shift = rnd.randint(1, 3)
        direction = 0  # up direction
        if new_x == self.x and new_y == self.y:
            return new_x, new_y
        if new_x > self.x:  # right direction
            direction = 1
        if new_y > self.y:  # down direction
            direction = 2
        if new_x < self.x:
            direction = 3  # left direction
        direction += shift
        direction %= 4
        if direction == 0 and self.y > 0 and game_map[self.y - 1][self.x] != b'#':
            return self.x, self.y - 1
        if direction == 1 and self.y < len(game_map) - 1 and game_map[self.y + 1][self.x] != b'#':
            return self.x, self.y + 1
        if direction == 2 and self.x < len(game_map[0]) - 1 and game_map[self.y][self.x + 1] != b'#':
            return self.x + 1, self.y
        if direction == 3 and self.x > 0 and game_map[self.y][self.x - 1] != b'#':
            return self.x - 1, self.y
        return self.x, self.y
