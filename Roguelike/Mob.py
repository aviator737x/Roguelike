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
            if map[y][x - 1] == b'.':
                return x - 1, y
            if yp < y and map[y - 1][x] == b'.':
                return x, y - 1
            if yp >= y and map[y + 1][x] == b'.':
                return x, y + 1
            else:
                return x, y
        if xp > x and abs(yp - y) <= x - xp:
            if map[y][x + 1] == b'.':
                return x + 1, y
            if yp < y and map[y - 1][x] == b'.':
                return x, y - 1
            if yp >= y and map[y + 1][x] == b'.':
                return x, y + 1
            else:
                return x, y
        if xp <= x and abs(yp - y) > x - xp:
            if yp < y and map[y - 1][x] == b'.':
                return x, y - 1
            if yp >= y and map[y + 1][x] == b'.':
                return x, y + 1
            if map[y][x - 1] == b'.':
                return x - 1, y
            else:
                return x, y
        if xp > x and abs(yp - y) > x - xp:
            if yp < y and map[y - 1][x] == b'.':
                return x, y - 1
            if yp >= y and map[y + 1][x] == b'.':
                return x, y + 1
            if map[y][x + 1] == b'.':
                return x + 1, y
            else:
                return x, y


class Cowardly(Strategy):
    @staticmethod
    def get_desired_position(x, y, map, xp, yp):
        if xp <= x and abs(yp - y) <= x - xp:
            if map[y][x + 1] == b'.':
                return x + 1, y
            if yp < y and map[y + 1][x] == b'.':
                return x, y + 1
            if yp >= y and map[y - 1][x] == b'.':
                return x, y - 1
            else:
                return x, y
        if xp > x and abs(yp - y) <= x - xp:
            if map[y][x - 1] == b'.':
                return x - 1, y
            if yp < y and map[y + 1][x] == b'.':
                return x, y + 1
            if yp >= y and map[y - 1][x] == b'.':
                return x, y - 1
            else:
                return x, y
        if xp <= x and abs(yp - y) > x - xp:
            if yp < y and map[y + 1][x] == b'.':
                return x, y + 1
            if yp >= y and map[y - 1][x] == b'.':
                return x, y - 1
            if map[y][x + 1] == b'.':
                return x + 1, y
            else:
                return x, y
        if xp > x and abs(yp - y) > x - xp:
            if yp < y and map[y + 1][x] == b'.':
                return x, y + 1
            if yp >= y and map[y - 1][x] == b'.':
                return x, y - 1
            if map[y][x - 1] == b'.':
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
        self.array_symbol = bytes(symbol_for_strategy[strategy], encoding='utf-8')
        if strategy == 0:
            self.strategy = Aggressive
        elif strategy == 1:
            self.strategy = Cowardly
        else:
            self.strategy = Passive

    def get_desired_position(self, map, player_coords):
        return self.strategy.get_desired_position(self.x, self.y, map, player_coords[0], player_coords[1])
