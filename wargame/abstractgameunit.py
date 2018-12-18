#!/usr/bin/env python
# -*- Coding：utf-8 -*-
"""
《python应用开发实战》
"""

from abc import ABCMeta, abstractmethod
from collections import Callable

from gameuniterror import GameUnitError
from gameutils import *
from jumpstrategy import can_not_jump
from accessoryfactory import AccessoryFactory


class AbstractGameUnit(metaclass=ABCMeta):
    factory = AccessoryFactory          # 抽象工厂，用于添加装备

    def __init__(self, name='', jump_strategy=can_not_jump):
        self.name = name                  # 表示NPC人物的“名号”
        self.max_hp = 0
        self.health_meter = 0
        self.enemy = None
        self.unit_type = None              # 表示NPC人物的阵营
        self.accessories = []                 # NPC人物的装备列表

        # 应用策略模型实现对GameUnit的跳跃能力的指派
        assert (isinstance(jump_strategy, Callable))  # 确保jump_strategy是一个函数
        self.jump = jump_strategy                         # 将函数jump_strategy赋值给变量self.jump

    @abstractmethod
    def info(self):
        """'Information on the unit (overridden in subclasses)'"""
        pass

    def show_accessories(self, bold=False, end='\n'):
        """Show the accessory list of the GameUnit """
        msg = "%s的装备:  " % (self.name)
        msg += '，'.join(str(item) for item in self.accessories)

        if bold:
            print_bold(msg, end=end)
        else:
            print(msg, end=end)

    def show_health(self, bold=False, end='\n'):
        """Show the remaining hit points of the GameUnit """
        msg = "%s的生命值: %d" % (self.name, self.health_meter)
        if bold:
            print_bold(msg, end=end)
        else:
            print(msg, end=end)

    def show_health_comparison(self, bold=False, end='\n'):
        """Show  comparison of the remaining hit points of the GameUnit and his enemy"""
        assert self.enemy, "Show health failed: No enemy facing now."
        self.show_health(bold, end='\t  VS.\t ')
        self.enemy.show_health(bold, end)

    def reset_health_meter(self):
        """Reset the `health_meter` (assign default hit points to GameUnit)"""
        self.health_meter = self.max_hp

    def show_details(self):
        self.show_health()
        self.show_accessories()

    def attack(self):
        """ This function is used for GameUnit to attack his enemy.  The self.enemy must be setup in advance """
        assert self.enemy, "Attack failed: No enemy facing now."

        injured_unit = weighted_random_selection(self, self.enemy)
        if injured_unit:
            injury = random.randint(10, 15)
            injured_unit.health_meter = max(injured_unit.health_meter - injury, 0)
        print("攻击! ", end='\n')
        self.show_health_comparison(bold=True)

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

    def equip_with_accessory(self, accessory_type):
        """ This function is used to equip with accessory , such as armor """
        accessory = type(self).factory.create_accessory(accessory_type)
        print_bold('{0}获得装备: {1} '.format(self.name, accessory))
        self.accessories.append(accessory)






