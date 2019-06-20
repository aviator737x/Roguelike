from asciimatics.screen import Screen
import asciimatics.event as event
import time

class InputHandler:
    def __init__(self, environment):
        self.environment = environment
        Screen.wrapper(self.run)

    def print_map(self, screen):
        x = 0
        y = 0
        for i in range(len(self.environment.map)):
            for j in range(len(self.environment.map[i])):
                symbol_table = self.environment.symbols_on_map
                symbol = symbol_table[self.environment.map[i][j]]
                screen.print_at(symbol, j, i)
        screen.refresh()

    def print_lost(self, screen):
        screen.print_at("You lost", 1, 1)
        screen.refresh()
        time.sleep(3)

    def run(self, screen):
        try:
            while True:
                self.print_map(screen)
                key = screen.get_event()
                if isinstance(key, event.KeyboardEvent):
                    code = self.environment.update(key)
                    if code:
                        self.print_lost(screen)
                        break
        except KeyboardInterrupt:
            return
