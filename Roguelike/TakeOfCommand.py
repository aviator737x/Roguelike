from Command import *
from RogueConstants import takeof_commands


class TakeOfCommand(Command):
    def __init__(self, environment, option):
        super().__init__(environment, option)

    def execute(self):
        self.environment.player.take_of(takeof_commands[self.option])
        return 0
