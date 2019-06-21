from Character import *


class Cell:
    def __init__(self, symbol):
        self.is_wall = False
        self.free_to_move = True
        self.is_empty = True
        if symbol == b'#':
            self.is_wall = True
            self.free_to_move = False
            self.is_empty = False
        self.map_object = None

    def set_object(self, map_object):
        self.is_empty = False
        self.map_object = map_object

    def clear_cell(self):
        self.free_to_move = True
        self.is_empty = True
        self.map_object = None
