class MapObject:
    def __init__(self):
        self.symbol = ' '
        self.array_symbol = b' '
        self.x = 0
        self.y = 0
        self.is_character = True

    def set_position(self, x, y):
        self.x = x
        self.y = y