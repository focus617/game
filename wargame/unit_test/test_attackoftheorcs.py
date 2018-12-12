#!/usr/bin/env python
# -*- Coding：utf-8 -*-

"""
《python应用开发实战》
兽人之袭v2.0.面向对象编程的单元测试
"""

import unittest
from unittest import mock

from abstractgameunit import AbstractGameUnit
from attackoftheorcs import AttackofTheOrcs, hut_number


class TestAttackofTheOrcs(unittest.TestCase):
    """ This class contains the unit testcase for game 'Attack of the Orcs' """

    def setUp(self):
        """ overrides the setUp fixture of the superclass. """
        self.game = AttackofTheOrcs()

    def test_occupy_huts(self):
        """ unit test to verify the hut occupant after it is initially occupied """
        self.game.setup_game_scenario()

        # verify that when hut is occupied in setup_game_scenario(),
        # the hut number is equal to hut_number
        self.assertEqual(len(self.game.huts), hut_number)

        # the 'hut.occupant' is instance of AbstractGameUnit.
        for hut in self.game.huts:
            assert(hut.occupant is None) or isinstance(hut.occupant, AbstractGameUnit)

    def test_play(self):
        pass


if __name__ == '__main__':
    # self-test code
    unittest.main()
