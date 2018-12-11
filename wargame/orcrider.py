#!/usr/bin/env python
# -*- Coding：utf-8 -*-
"""
《python应用开发实战》
"""

from .abstractgameunit import AbstractGameUnit


class OrcRider(AbstractGameUnit):

    def __init__(self, name=''):
        super().__init__(name=name)
        self.max_hp = 30
        self.health_meter = self.max_hp
        self.unit_type = '敌人'
        # self.hut_number = 0

    def info(self):
        print('%s: "啊啊啊啊！兽人永不为奴！别惹我"' % self.name)








