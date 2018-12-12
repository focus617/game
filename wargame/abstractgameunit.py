#!/usr/bin/env python
# -*- Coding：utf-8 -*-
"""
《python应用开发实战》
"""

from abc import ABCMeta, abstractmethod

from gameuniterror import GameUnitError
from gameutils import *

class AbstractGameUnit(metaclass=ABCMeta):

    def __init__(self, name=''):
        self.name = name
        self.max_hp = 0
        self.health_meter = 0
        self.enemy = None
        self.unit_type = None  # 表示NPC人物的阵营

    @abstractmethod
    def info(self):
        """'Information on the unit (overridden in subclasses)'"""
        pass

    def show_health(self, bold=False, end='\n'):
        """Show the remaining hit points of the player and the enemy"""
        msg = "%s的生命值: %d" % (self.name, self.health_meter)
        if bold:
            print_bold(msg, end=end)
        else:
            print(msg, end=end)

    def reset_health_meter(self):
        """Reset the `health_meter` (assign default hit points)"""
        self.health_meter = self.max_hp

    def attack(self, enemy):
        injured_unit = weighted_random_selection(self, enemy)
        if injured_unit:
            injury = random.randint(10, 15)
            injured_unit.health_meter = max(injured_unit.health_meter - injury, 0)
        print("攻击! ", end='\n')
        self.show_health(end='  ')
        enemy.show_health(end='  ')

    def heal(self, heal_by=2, full_healing=True):
        """Heal the unit replenishing all the hit points"""
        if self.health_meter == self.max_hp:
            return
        else:
            print_bold("需要治疗：", end='')
            self.show_health()
            print_bold("治疗中.........", end='\n')

        if full_healing:
            self.health_meter = self.max_hp
        else:
            self.health_meter += heal_by

        if self.health_meter > self.max_hp:
            raise GameUnitError('治疗恢复值无效, 超过最大允许值', code=101)

        print_bold("已被治疗!", end=' ')
        self.show_health(bold=True)









