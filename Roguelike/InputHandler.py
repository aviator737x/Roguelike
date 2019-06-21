from asciimatics.screen import Screen
import asciimatics.event as event
import time
import codecs
import os
from Command.CheckBackpack import *
from Command.TakeOfCommand import *
from Command.WearCommand import *
from Command.MovingCommand import *
from Command.ExitCommand import *


class InputHandler:
    """
    Class for handling input keys and printing current window
    """
    def __init__(self, environment):
        self.environment = environment
        Screen.wrapper(self.run)

    def print_map(self, screen):
        """
        print current environment window
        :param screen: Screen to print symbols on
        :return: None
        """
        window = self.environment.window.window
        x = 0
        y = 0
        for i in range(len(window)):
            for j in range(len(window[i])):
                symbol_table = self.environment.symbols_on_map
                if isinstance(window[i][j], str):
                    symbol = window[i][j]
                else:
                    symbol = codecs.decode(window[i][j])
                if symbol == '':
                    screen.print_at(" ", j, i, transparent=False)
                else:
                    screen.print_at(symbol, j, i, transparent=False)
        screen.refresh()

    def parseCommand(self, key):
        if key.key_code == Screen.KEY_UP:
            return MovingCommand(self.environment, "up")
        if key.key_code == Screen.KEY_DOWN:
            return MovingCommand(self.environment, "down")
        if key.key_code == Screen.KEY_LEFT:
            return MovingCommand(self.environment, "left")
        if key.key_code == Screen.KEY_RIGHT:
            return MovingCommand(self.environment, "right")
        if key.key_code == ord("w") or key.key_code == ord("e") or key.key_code == ord("r"):
            return WearCommand(self.environment, chr(key.key_code))
        if key.key_code == ord("s") or key.key_code == ord("d") or key.key_code == ord("f"):
            return TakeOfCommand(self.environment, chr(key.key_code))
        if key.key_code == ord('b'):
            return CheckBackpackCommand(self.environment, 'b')
        if key.key_code == ord('x'):
            return ExitCommand(self.environment, "")
        if key.key_code == ord('c'):
            return ExitCommand(self.environment, "save")
        return None

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
                    command = self.parseCommand(key)
                    if command is not None:
                        code = command.execute()
                        if code == 1:
                            self.print_lost(screen)
                            if os.path.exists("saved_game.txt"):
                                os.remove("saved_game.txt")
                        if code:
                            break
        except KeyboardInterrupt:
            return
