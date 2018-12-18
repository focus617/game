#!/usr/bin/env python
# -*- Coding：utf-8 -*-

"""
《python应用开发实战》
兽人之袭v2.0.面向对象编程的单元测试
"""

import unittest

from knight import Knight
from orcrider import OrcRider
from accessoryfactory import IronJacket, OrcPowerSuit
from jumpstrategy import can_not_jump, horse_jump, power_jump


class TestGameUnit(unittest.TestCase):
    """ This class contains the unit testcase for game 'Attack of the Orcs' """

    def setUp(self):
        """ overrides the setUp fixture of the superclass. """
        self.knight = Knight(name='Foo')
        self.enemy = OrcRider()

    def test_reset_health_meter(self):
        """ unit test fo verify if the health_meter was assigned to default hit points of GameUnit"""
        self.knight.health_meter = 1
        self.knight.reset_health_meter()
        self.assertEqual(self.knight.health_meter, self.knight.max_hp)

    def test_heal_full_healing(self):
        """ unit test fo verify if the health_meter was assigned to default hit points of GameUnit"""
        self.knight.health_meter = 1
        self.knight.heal(full_healing=True)
        self.assertEqual(self.knight.health_meter, self.knight.max_hp)

    def test_heal_partial_healing(self):
        """ unit test fo verify if the health_meter was increased with default  heal_by hit points  """
        self.knight.health_meter = 1
        self.knight.heal(full_healing=False)
        self.assertEqual(self.knight.health_meter, 3)

    def test_show_health_comparison(self):
        self.knight.enemy = None
        with self.assertRaises(AssertionError):
            self.knight.show_health_comparison()

    def test_jump(self):
        self.assertEqual(self.knight.jump, horse_jump)
        self.assertEqual(self.enemy.jump, power_jump)

    def test_attack(self):
        self.knight.enemy = None
        with self.assertRaises(AssertionError):
            self.knight.attack()

    def test_equip_with_accessory_knight(self):
        self.assertEqual (len(self.knight.accessories), 0)
        self.knight.equip_with_accessory('ironjacket')
        self.assertIsInstance(self.knight.accessories[0], IronJacket)

    def test_equip_with_accessory_orc(self):
        self.assertEqual (len(self.enemy.accessories), 0)
        self.enemy.equip_with_accessory('powersuit')
        self.assertIsInstance(self.enemy.accessories[0], OrcPowerSuit)


if __name__ == '__main__':
    # self-test code
    unittest.main()
