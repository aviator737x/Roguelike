import numpy as np


class MapGenerator:
    def __init__(self, size):
        self.size = size

    def generate_map(self):
        grid = np.random.sample((self.size, self.size))
        free_area_coef = 0.55
        for i in range(self.size):
            for j in range(self.size):
                if grid[i][j] < free_area_coef:
                    grid[i][j] = 0
                else:
                    grid[i][j] = 1

        # cells on edges are walls
        grid[0] = np.ones(shape=(self.size,))
        grid[-1] = np.ones(shape=(self.size,))
        grid[..., 0] = np.ones(shape=(self.size,))
        grid[..., -1] = np.ones(shape=(self.size,))
        grid = self.__recompute_grid(grid)
        return self.__grid_to_char(grid)

    def __recompute_grid(self, grid):
        smth_changed = True
        while smth_changed:
            smth_changed = False
            new_grid = np.copy(grid)
            for i in range(1, len(grid) - 1):
                for j in range(len(grid) - 1):
                    neighbours = np.array([grid[i - 1][j - 1], grid[i - 1][j], grid[i - 1][j + 1],
                                           grid[i][j - 1], grid[i][j + 1],
                                           grid[i + 1][j - 1], grid[i + 1][j], grid[i + 1][j + 1]])
                    open_neighbours = len(np.where(neighbours == 1)[0])
                    if open_neighbours > 5:
                        new_grid[i][j] = 1
                    if open_neighbours < 3:
                        new_grid[i][j] = 0
                    if new_grid[i][j] != grid[i][j]:
                        smth_changed = True
            grid = new_grid
        return grid

    def __grid_to_char(self, grid):
        char_grid = np.empty(shape=(self.size, self.size), dtype='S')
        for i in range(self.size):
            for j in range(self.size):
                if grid[i][j]:
                    char_grid[i][j] = '#'
                else:
                    char_grid[i][j] = '.'
        return char_grid
