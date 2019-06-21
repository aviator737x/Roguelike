from Cell import *
from Window import *
import numpy as np


class GameMap(Window):
    def __init__(self, map_grid):
        super().__init__(map_grid.shape)
        self.cells = np.empty(shape=map_grid.shape, dtype=object)
        for row in range(len(self.cells)):
            for column in range(len(self.cells[row])):
                self.cells[row][column] = Cell(map_grid[row][column])
        self.draw()

    def draw(self):
        for row in range(len(self.window)):
            for column in range(len(self.window[row])):
                cell = self.cells[row][column]
                if cell.is_wall:
                    self.window[row][column] = '#'
                    continue
                if cell.is_empty:
                    self.window[row][column] = '.'
                    continue
                if cell.map_object is not None:
                    self.window[row][column] = cell.map_object.symbol

    def set_object(self, map_object, row, column):
        self.cells[row][column].set_object(map_object)

    def clear_cell(self, row, column):
        self.cells[row][column].clear_cell()