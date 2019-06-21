from Command.Command import *


class CheckBackpackCommand(Command):
    def __init__(self, environment, option):
        super().__init__(environment, option)

    def execute(self):
        self.environment.check_uncheck_backpack()
        return 0