from MapObjects.Character.Character import *

symbol_for_strategy = ['%', '*', '&']


class Strategy:
    @staticmethod
    def get_desired_position(x, y, map_cells, xp, yp):
        pass


class Aggressive(Strategy):
    @staticmethod
    def get_desired_position(x, y, map_cells, xp, yp):
        if xp <= x and abs(yp - y) <= x - xp:
            if map_cells[y][x - 1].free_to_move:
                return x - 1, y
            if yp < y and map_cells[y - 1][x].free_to_move:
                return x, y - 1
            if yp >= y and map_cells[y + 1][x].free_to_move:
                return x, y + 1
            else:
                return x, y
        if xp > x and abs(yp - y) <= x - xp:
            if map_cells[y][x + 1].free_to_move:
                return x + 1, y
            if yp < y and map_cells[y - 1][x].free_to_move:
                return x, y - 1
            if yp >= y and map_cells[y + 1][x].free_to_move:
                return x, y + 1
            else:
                return x, y
        if xp <= x and abs(yp - y) > x - xp:
            if yp < y and map_cells[y - 1][x].free_to_move:
                return x, y - 1
            if yp >= y and map_cells[y + 1][x].free_to_move:
                return x, y + 1
            if map_cells[y][x - 1].free_to_move:
                return x - 1, y
            else:
                return x, y
        if xp > x and abs(yp - y) > x - xp:
            if yp < y and map_cells[y - 1][x].free_to_move:
                return x, y - 1
            if yp >= y and map_cells[y + 1][x].free_to_move:
                return x, y + 1
            if map_cells[y][x + 1].free_to_move:
                return x + 1, y
            else:
                return x, y


class Cowardly(Strategy):
    @staticmethod
    def get_desired_position(x, y, map_cells, xp, yp):
        if xp <= x and abs(yp - y) <= x - xp:
            if map_cells[y][x + 1].free_to_move:
                return x + 1, y
            if yp < y and map_cells[y + 1][x].free_to_move:
                return x, y + 1
            if yp >= y and map_cells[y - 1][x].free_to_move:
                return x, y - 1
            else:
                return x, y
        if xp > x and abs(yp - y) <= x - xp:
            if map_cells[y][x - 1].free_to_move:
                return x - 1, y
            if yp < y and map_cells[y + 1][x].free_to_move:
                return x, y + 1
            if yp >= y and map_cells[y - 1][x].free_to_move:
                return x, y - 1
            else:
                return x, y
        if xp <= x and abs(yp - y) > x - xp:
            if yp < y and map_cells[y + 1][x].free_to_move:
                return x, y + 1
            if yp >= y and map_cells[y - 1][x].free_to_move:
                return x, y - 1
            if map_cells[y][x + 1].free_to_move:
                return x + 1, y
            else:
                return x, y
        if xp > x and abs(yp - y) > x - xp:
            if yp < y and map_cells[y + 1][x].free_to_move:
                return x, y + 1
            if yp >= y and map_cells[y - 1][x].free_to_move:
                return x, y - 1
            if map_cells[y][x - 1].free_to_move:
                return x - 1, y
            else:
                return x, y


class Passive(Strategy):
    @staticmethod
    def get_desired_position(x, y, map_cells, xp, yp):
        return x, y


class Mob(Character):
    def __init__(self, strategy):
        Character.__init__(self)
        self.symbol = symbol_for_strategy[strategy]
        self.array_symbol = bytes(symbol_for_strategy[strategy], encoding='utf-8')
        if strategy == 0:
            self.strategy = Aggressive
        elif strategy == 1:
            self.strategy = Cowardly
        else:
            self.strategy = Passive

    def get_desired_position(self, map_cells, player_coords):
        return self.strategy.get_desired_position(self.x, self.y, map_cells, player_coords[0], player_coords[1])
