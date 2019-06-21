from Command import *


class MovingCommand(Command):
    def __init__(self, environment, direction):
        super().__init__(environment, direction)

    def execute(self):
        return self.environment.update(self.option)
