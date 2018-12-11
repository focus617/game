#!/usr/bin/env python
# -*- Coding：utf-8 -*-
"""
《python应用开发实战》
"""

from .gameutils import *


class Hut:

    def __init__(self, index, occupant):
        self.id = index
        self.occupant = occupant
        self.is_acquired = False    # 标识木屋是否被占领

    def acquire(self, new_occupant):
        self.occupant = new_occupant
        self.is_acquired = True
        print_bold('干得好！%d号木屋已经被调查' % self.id)

    def get_occupant_type(self):
        if self.is_acquired:
            occupant_type = '已被调查'
        elif self.occupant is None:
            occupant_type = '无人居住'
        else:
            occupant_type = self.occupant.unit_type
        return occupant_type








