#!/usr/bin/env python
# -*- Coding：utf-8 -*-
"""
《python应用开发实战》
"""

from gameutils import *
from abstractgameunit import AbstractGameUnit


class Knight(AbstractGameUnit):

    def __init__(self, name='Foo先生'):
        super().__init__(name=name)  # 调用超类的初始化函数
        self.max_hp = 40
        self.health_meter = self.max_hp
        self.unit_type = '朋友'

    def info(self):
        print('%s: "我是一名骑士!"' % self.name)

    def acquire_hut(self, hut):
        """ Fight the combat (command line) to acquire the hut"""
        print_bold('进入%d号木屋' % hut.id, end=' ')

        # 判断木屋占有者是否是敌人
        is_enemy = (isinstance(hut.occupant, AbstractGameUnit)
                    and hut.occupant.unit_type == '敌人')
        continue_attack = 'y'
        if is_enemy:
            print_bold('发现敌人！')
            self.enemy = hut.occupant
            self.enemy.info()
            self.show_health_comparison(bold=True)
            while continue_attack:
                try:
                    continue_attack = input('\n.......是否继续攻击？(y/n): ')
                    assert (continue_attack in ['y', 'Y', 'n', 'N'])
                except AssertionError:
                    print('无效输入！')
                    continue_attack = 'y'
                    continue

                # 逃跑或者继续攻击
                if continue_attack.lower() == 'n':
                    self.runaway()
                    break
                else:
                    self.attack()

                if self.enemy.health_meter <= 0:
                    print(' ')
                    hut.acquire(self)
                    self.enemy = None
                    break

                if self.health_meter <= 0:
                    print(' ')
                    break
        else:
            if hut.get_occupant_type() == '无人居住':
                print_bold('木屋无人居住')
            else:
                print_bold('找到一个朋友')
                self.heal()

                # 测试异常的情况：如果heal_by>40，导致health_meter超过最大值
                # try:
                #     self.heal(heal_by=100, full_healing=False)
                # except GameUnitError as e:
                #     print(e.error_message)
                #     self.heal()

            hut.acquire(self)

    def runaway(self):
        print_bold('溜了溜了...')
        self.enemy = None








