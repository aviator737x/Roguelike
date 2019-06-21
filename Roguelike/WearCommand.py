from Command import *
from RogueConstants import wear_commands


class WearCommand(Command):
    def __init__(self, environment, option):
        super().__init__(environment, option)

    def execute(self):
        self.environment.player.wear_from_backpack(wear_commands[self.option])
        return 0