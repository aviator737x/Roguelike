import random as rnd

from MapObjects.Character.Player import *


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

    def get_desired_position(self, map_cells, direction):
        new_x, new_y = self.player.get_desired_position(map_cells, direction)
        if self.duration == 0:
            return new_x, new_y
        self.duration -= 1
        shift = rnd.randint(1, 3)
        chosen_direction = 0  # up direction
        if new_x == self.x and new_y == self.y:
            return new_x, new_y
        if new_x > self.x:  # right direction
            chosen_direction = 1
        if new_y > self.y:  # down direction
            chosen_direction = 2
        if new_x < self.x:
            chosen_direction = 3  # left direction
        chosen_direction += 2
        chosen_direction += shift
        chosen_direction %= 4
        if chosen_direction == 0 and self.y > 0 and map_cells[self.y - 1][self.x].free_to_move:
            return self.x, self.y - 1
        if chosen_direction == 1 and self.y < len(map_cells) - 1 and map_cells[self.y + 1][self.x].free_to_move:
            return self.x, self.y + 1
        if chosen_direction == 2 and self.x < len(map_cells[0]) - 1 and map_cells[self.y][self.x + 1].free_to_move:
            return self.x + 1, self.y
        if chosen_direction == 3 and self.x > 0 and map_cells[self.y][self.x - 1].free_to_move:
            return self.x - 1, self.y
        return self.x, self.y
