#!/usr/bin/env python
# -*- Coding：utf-8 -*-
"""
《python应用开发实战》
"""

from gameutils import *


# 人类的盔甲, 挂件
class IronJacket:
    def __str__(self):
        return 'IronJacket'


class PowerSuit:
    pass


class MithrilArmor:
    pass


class GlodLocket:
    pass


class SuperLokcet:
    pass


class MagicLocket:
    pass


# 兽人的盔甲, 挂件
class OrcIronJacket:
    pass


class OrcPowerSuit:
    pass


class OrcMithrilArmor:
    pass


class OrcGlodLocket:
    pass


class OrcSuperLokcet:
    pass


class OrcMagicLocket:
    pass

class AccessoryFactory:
    accessory_dict = {
        'ironjacket': IronJacket,
        'powersuit': PowerSuit,
        'mithril'     : MithrilArmor,
        'goldlocket': GlodLocket,
        'superlocket':SuperLokcet,
        'magiclocket':MagicLocket
    }

    @classmethod
    def create_accessory(cls, accessory_type):
        print_bold('获得%s装备' % accessory_type.upper())
        return cls.accessory_dict.get(accessory_type)()   # 根据armor_type创建具体的盔甲类实例


class OrcAccessoryFactory(AccessoryFactory):
    accessory_dict = {
        'ironjacket': OrcIronJacket,
        'powersuit': OrcPowerSuit,
        'mithril'     : OrcMithrilArmor,
        'goldlocket': OrcGlodLocket,
        'superlocket': OrcSuperLokcet,
        'magiclocket': OrcMagicLocket
    }













