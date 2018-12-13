#!/usr/bin/env python
# -*- Coding：utf-8 -*-
"""
《python应用开发实战》
"""

from gameutils import *


# 人类的盔甲
class IronJacket:
    def __str__(self):
        return 'IronJacket'


class PowerSuit:
    pass


class MithrilArmor:
    pass


# 兽人的盔甲
class OrcIronJacket:
    pass


class OrcPowerSuit:
    pass


class OrcMithrilArmor:
    pass


class AccessoryFactory:
    armor_dict = {
        'ironjacket': IronJacket,
        'powersuit': PowerSuit,
        'mithril'     : MithrilArmor
    }

    @classmethod
    def create_armor(cls, armor_type):
        print_bold('%s型盔甲已被装备' % armor_type.upper())
        return cls.armor_dict.get(armor_type)()   # 根据armor_type创建具体的盔甲类实例


class OrcAccessoryFactory(AccessoryFactory):
    armor_dict = {
        'ironjacket': OrcIronJacket,
        'powersuit': OrcPowerSuit,
        'mithril'     : OrcMithrilArmor
    }













