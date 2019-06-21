from Window import *
import numpy as np


class BackpackWindow(Window):
    def __init__(self, window_size):
        super().__init__(window_size)
        self.backpack = dict()

    def set_backpack(self, backpack):
        self.backpack = backpack
        self.clear_window()
        self.print_string(0, "Your items:")
        row = 1
        for inventory_name, lst in self.backpack.items():
            if lst:
                to_print = inventory_name + ": " + str(len(lst))
                self.print_string(row, to_print)
                row += 1
