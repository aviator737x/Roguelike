from Command import *


class ExitCommand(Command):
    def __init__(self, environment, option):
        super().__init__(environment, option)

    def execute(self):
        if self.option == "save":
            self.environment.write_to_file("saved_game.txt")
            return 2
        return 3