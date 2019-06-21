import numpy as np


class MapLoader:
    def __init__(self, filename):
        self.filename = filename

    def generate_map(self):
        lines = []
        with open(self.filename) as file:
            for line in file:
                lines.append(line)
        grid = np.empty(shape=(len(lines), len(lines[0]) - 1), dtype='S')
        for i in range(len(lines)):
            for j in range(len(lines[0]) - 1):
                grid[i][j] = lines[i][j]
        return grid
