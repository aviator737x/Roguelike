class Character:
    def __init__(self):
        self.symbol = ' '
        self.array_symbol = b' '
        self.x = 0
        self.y = 0

    def set_position(self, x, y):
        self.x = x
        self.y = y

    # TODO: implement battle
    # Empty set if nobody wins
    @staticmethod
    def battle(players):
        return set()
