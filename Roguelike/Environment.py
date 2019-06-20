import numpy as np
import random as rnd

from Player import *
from Mob import *
from ConfusionDecorator import *


class Environment:
    def __init__(self, game_map):
        rnd.seed()
        self.map = game_map
        self.player = Player()
        self.symbols_on_map = {
            b'.': '.',
            b'#': '#'
        }
        self.position_character(self.player)
        self.mobs = set()

    def position_character(self, character):
        empty_cells = np.where(self.map == b'.')
        num_of_empty_cells = len(empty_cells[0])
        cell_to_place = rnd.randrange(0, num_of_empty_cells)
        y = empty_cells[0][cell_to_place]
        x = empty_cells[1][cell_to_place]
        self.map[y][x] = character.symbol
        self.symbols_on_map[character.array_symbol] = character.symbol
        character.set_position(x, y)

    def confuse_player(self):
        self.player = ConfusionDecorator(self.player, 10)

    # random mob creation here
    def before_update(self):
        rand_number = rnd.randint(1, 50)
        if rand_number == 1:
            self.confuse_player()
        rand_number = rnd.randint(1, 4)
        if rand_number == 1:
            rand_strategy = rnd.randint(0, 2)
            mob = Mob(rand_strategy)
            self.position_character(mob)
            self.mobs.add(mob)

    def update(self, input_symbol):
        self.before_update()
        new_map = [[set() for _ in range(len(self.map[i]))] for i in range(len(self.map))]
        for mob in self.mobs:
            new_x, new_y = mob.get_desired_position(self.map, (self.player.x, self.player.y))
            new_map[new_x][new_y].add(mob)
        new_x, new_y = self.player.get_desired_position(self.map, input_symbol)
        new_map[new_y][new_x].add(self.player)
        resolve_collisions = True
        while resolve_collisions:
            resolve_collisions = False
            for row in range(len(new_map)):
                for column in range(len(new_map[0])):
                    if len(new_map[row][column]) > 1:  # more than one character tries to place cell
                        fighters = new_map[row][column]
                        loosers = Character.battle(fighters)
                        if loosers:
                            for looser in loosers:
                                self.mobs.remove(looser)
                                fighters.remove(looser)
                                if looser == self.player:
                                    return 1

                        if not loosers or len(fighters) > 1:
                            resolve_collisions = True
                            fighters.clear()

        for row in range(len(new_map)):
            for column in range(len(new_map[0])):
                if new_map[row][column]:
                    character = new_map[row][column].pop()
                    self.map[row][column] = character.symbol
                    character.set_position(column, row)
                elif self.map[row][column] != b'#':
                    self.map[row][column] = '.'

        return 0
