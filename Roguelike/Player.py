from Character import Character
from asciimatics.screen import Screen


class Player(Character):
    def __init__(self):
        super().__init__()
        self.symbol = '@'
        self.array_symbol = b'@'

    def get_desired_position(self, game_map, key):
        if key.key_code == Screen.KEY_UP and self.y > 0 and game_map[self.y - 1][self.x] != b'#':
            return self.x, self.y - 1
        if key.key_code == Screen.KEY_DOWN and self.y < len(game_map) - 1 and game_map[self.y + 1][self.x] != b'#':
            return self.x, self.y + 1
        if key.key_code == Screen.KEY_RIGHT and self.x < len(game_map[0]) - 1 and game_map[self.y][self.x + 1] != b'#':
            return self.x + 1, self.y
        if key.key_code == Screen.KEY_LEFT and self.x > 0 and game_map[self.y][self.x - 1] != b'#':
            return self.x - 1, self.y
        return self.x, self.y
