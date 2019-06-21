import numpy as np


class Window:
    def __init__(self, window_size):
        self.window = np.chararray(shape=window_size)
        self.clear_window()

    def print_string(self, row, to_print):
        if row >= len(self.window):
            return
        for i in range(min(len(to_print), len(self.window[0]))):
            self.window[row][i] = to_print[i]

    def clear_window(self):
        self.window[:] = ' '
