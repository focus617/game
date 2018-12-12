#!/usr/bin/env python
# -*- Coding：utf-8 -*-

"""
《python应用开发实战》
兽人之袭v2.0.面向对象编程的单元测试
"""

import unittest

from abstractgameunit import AbstractGameUnit
from knight import Knight
from orcrider import OrcRider
from hut import Hut
from gameutils import weighted_random_selection


class TestGameUtils(unittest.TestCase):
    """ This class contains the unit testcase for game 'Attack of the Orcs' """

    def setUp(self):
        """ overrides the setUp fixture of the superclass. """
        self.knight = Knight()
        self.enemy = OrcRider()

    def test_injured_unit_selection(self):
        """ unit test to verify working of weighted_random_selection() """
        # verify if the injured unit is an instance of class AbstractGameUnit
        for i in range(100):
            injured_unit = weighted_random_selection(self.knight, self.enemy)
            # self.assertIsInstance(injured_unit, AbstractGameUnit,
            #                       'Injured unit must be an instance of AbstractGameUnit')
            self.assertIn(injured_unit, [self.knight, self.enemy, None])


if __name__ == '__main__':
    # self-test code
    unittest.main()
