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


class TestHut(unittest.TestCase):
    """ This class contains the unit testcase for game 'Attack of the Orcs' """

    def setUp(self):
        """ overrides the setUp fixture of the superclass. """
        self.knight = Knight()
        self.enemy = OrcRider()

    def test_acquire_hut(self):
        """ unit test to verify the hut occupant after it is acquired """
        # verify that when hut is acquired by a Knight, the 'hut.occupant' is updated to the Knight instance.
        hut = Hut(2, None)
        hut.acquire(self.knight)
        self.assertIs(self.knight, hut.occupant)


if __name__ == '__main__':
    # self-test code
    unittest.main()
