from Character import Character

symbol_for_strategy = ['%', '*', '&']


class Strategy:
    @staticmethod
    def get_desired_position(x, y, map, xp, yp):
        pass


class Aggressive(Strategy):
    @staticmethod
    def get_desired_position(x, y, map, xp, yp):
        if xp <= x and abs(yp - y) <= x - xp:
            if map[x - 1][y] == '.':
                return x - 1, y
            if yp < y and map[x][y - 1] == '.':
                return x, y - 1
            if yp >= y and map[x][y + 1] == '.':
                return x, y + 1
            else:
                return x, y
        if xp > x and abs(yp - y) <= x - xp:
            if map[x + 1][y] == '.':
                return x + 1, y
            if yp < y and map[x][y - 1] == '.':
                return x, y - 1
            if yp >= y and map[x][y + 1] == '.':
                return x, y + 1
            else:
                return x, y
        if xp <= x and abs(yp - y) > x - xp:
            if yp < y and map[x][y - 1] == '.':
                return x, y - 1
            if yp >= y and map[x][y + 1] == '.':
                return x, y + 1
            if map[x - 1][y] == '.':
                return x - 1, y
            else:
                return x, y
        if xp > x and abs(yp - y) > x - xp:
            if yp < y and map[x][y - 1] == '.':
                return x, y - 1
            if yp >= y and map[x][y + 1] == '.':
                return x, y + 1
            if map[x + 1][y] == '.':
                return x + 1, y
            else:
                return x, y


class Cowardly(Strategy):
    @staticmethod
    def get_desired_position(x, y, map, xp, yp):
        if xp <= x and abs(yp - y) <= x - xp:
            if map[x + 1][y] == '.':
                return x + 1, y
            if yp < y and map[x][y + 1] == '.':
                return x, y + 1
            if yp >= y and map[x][y - 1] == '.':
                return x, y - 1
            else:
                return x, y
        if xp > x and abs(yp - y) <= x - xp:
            if map[x - 1][y] == '.':
                return x - 1, y
            if yp < y and map[x][y + 1] == '.':
                return x, y + 1
            if yp >= y and map[x][y - 1] == '.':
                return x, y - 1
            else:
                return x, y
        if xp <= x and abs(yp - y) > x - xp:
            if yp < y and map[x][y + 1] == '.':
                return x, y + 1
            if yp >= y and map[x][y - 1] == '.':
                return x, y - 1
            if map[x + 1][y] == '.':
                return x + 1, y
            else:
                return x, y
        if xp > x and abs(yp - y) > x - xp:
            if yp < y and map[x][y + 1] == '.':
                return x, y + 1
            if yp >= y and map[x][y - 1] == '.':
                return x, y - 1
            if map[x - 1][y] == '.':
                return x - 1, y
            else:
                return x, y


class Passive(Strategy):
    @staticmethod
    def get_desired_position(x, y, map, xp, yp):
        return x, y


class Mob(Character):
    def __init__(self, strategy):
        Character.__init__(self)
        self.symbol = symbol_for_strategy[strategy]
        self.array_symbol = 'b' + symbol_for_strategy[strategy]
        if strategy == 0:
            self.strategy = Aggressive
        elif strategy == 1:
            self.strategy = Cowardly
        else:
            self.strategy = Passive

    def get_desired_position(self, map, player_coords):
        return self.strategy.get_desired_position(self.x, self.y, map, player_coords[0], player_coords[1])

