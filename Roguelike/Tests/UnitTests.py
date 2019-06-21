from Environment import *
import unittest
import numpy as np


class TestMethods(unittest.TestCase):
    def test_decrease_hp_in_fight(self):
        mob = Mob(2)
        player = Player()
        old_hp_mob = mob.health
        old_hp_player = player.health
        fighters = set()
        fighters.add(mob)
        fighters.add(player)
        Character.battle(fighters)
        new_hp_mob = mob.health
        new_hp_player = player.health
        self.assertTrue(new_hp_mob < old_hp_mob and new_hp_player < old_hp_player)


if __name__ == '__main__':
    unittest.main()