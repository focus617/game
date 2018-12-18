#!/usr/bin/env python
# -*- Coding：utf-8 -*-
"""
《python应用开发实战》
"""

from abc import ABCMeta
from gameutils import *


class AbstractAccessory(metaclass=ABCMeta):
    """"  用于表示装备的抽象类 """
    def __init__(self, name=''):
        if name:
            self.name = name
        else:
            self.name = '白板'

    def __str__(self):
        return (self.__class__.__name__ + '-' + self.name)


# 人类的盔甲, 挂件
class IronJacket(AbstractAccessory):
    """
    >>> str(IronJacket())
    'IronJacket-白板'
    """
    pass


class PowerSuit(AbstractAccessory):
    pass


class MithrilArmor(AbstractAccessory):
    pass


class GlodLocket(AbstractAccessory):
    pass


class SuperLokcet(AbstractAccessory):
    pass


class MagicLocket(AbstractAccessory):
    pass


# 兽人的盔甲, 挂件
class OrcIronJacket(AbstractAccessory):
    pass


class OrcPowerSuit(AbstractAccessory):
    pass


class OrcMithrilArmor(AbstractAccessory):
    pass


class OrcGlodLocket(AbstractAccessory):
    pass


class OrcSuperLokcet(AbstractAccessory):
    pass


class OrcMagicLocket(AbstractAccessory):
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













