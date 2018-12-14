#!/usr/bin/env python
# -*- Coding：utf-8 -*-

# python应用开发实战
# 兽人之袭v1.0.面向对象编程
"""
需求分析：
1、获得所有木屋击败木屋里的所有敌人
2、可以在同伴或者无人居住的木屋中治疗自身
3、可以选择放弃战斗，在木屋中治疗后返回战斗
4、引入一个或者多个骑士帮助FOO先生，他们可以轮流占领木屋
5、可以为每个敌人和骑士配置最大的攻击点
6、木屋数量实现可配置
7、木屋中可以存放一些黄金或者武器，Foo先生和他的同伴可以捡起这把武器
8、可以让一个精灵骑士加入队伍，更大几率获胜
"""

from gameutils import *
from hut import Hut
from knight import Knight
from orcrider import OrcRider
from const import HUT_NUMBER


class AttackofTheOrcs:

    def __init__(self):
        self.huts = []
        self.player = None

    @staticmethod
    def show_game_mission():
        print_bold('任务1：')
        print('1、打败所有敌人')
        print('2、调查所有木屋，获取所有木屋的控制权')
        print_dotted_line()

    def get_occupants(self):
        return [x.get_occupant_type() for x in self.huts]

    def _occupy_huts(self):
        """Randomly occupy the hut with one of : friend, enemy or None"""
        for i in range(HUT_NUMBER):
            choice_list = ['敌人', '朋友', None]
            computer_choice = random.choice(choice_list)
            # 根据计算机随机选择木屋里是敌人、队友或是空的
            if computer_choice == '敌人':
                name = '敌人-' + str(i + 1)
                self.huts.append(Hut(i + 1, OrcRider(name)))
            elif computer_choice == '朋友':
                name = '骑士-' + str(i + 1)
                self.huts.append(Hut(i + 1, Knight(name)))
            else:
                self.huts.append(Hut(i + 1, computer_choice))

    def _process_user_choice(self):
        """"Process the user input for choice of hut to enter"""
        print("木屋调查情况: %s" % self.get_occupants())

        idx = 0
        verifying_choice = True
        while verifying_choice:
            user_choice = input('选择一个木屋进入(1-%d):' % HUT_NUMBER)
            #  exception process for non-integer user_choice
            try:
                idx = int(user_choice)
            except ValueError as e:
                print('无效输入，参数不是整数（ %s ）' % e.args)
                continue

            try:
                assert idx > 0
                if self.huts[idx - 1].is_acquired:
                    print('你已经调查过这个木屋，请再尝试一次。\n'
                          '提示：不能再已调查的木屋得到治疗')
                else:
                    verifying_choice = False
            except IndexError:
                print('无效输入，你输入的木屋号超过了可选择范围（1-%d)！' % HUT_NUMBER)
                continue
            # If idx <= 0
            except AssertionError:
                print('无效输入，你输入的木屋号超过了可选择范围（1-%d)！' % HUT_NUMBER)
                continue

        return idx

    def setup_game_scenario(self):
        """ Create player - a Knight and huts, then randomly pre-occupy huts """
        self.player = Knight()
        self.player.info()
        self.player.show_health(bold=False)
        self._occupy_huts()

    def play(self):
        """" Workhorse method to play the game"""
        # Initialize the game setup
        self.show_game_mission()
        self.setup_game_scenario()

        # main game play logic begins
        acquires_hut_counter = 0
        while acquires_hut_counter < HUT_NUMBER:
            idx = self._process_user_choice()
            self.player.acquire_hut(self.huts[idx-1])

            if self.player.health_meter <= 0:
                print_bold('你输了！祝下次好运！')
                break

            if self.huts[idx-1].is_acquired:
                acquires_hut_counter += 1

        if acquires_hut_counter == HUT_NUMBER:
            print_bold('祝贺你！你已经调查完所有的木屋')


if __name__ == '__main__':
    show_theme_message()

    game = AttackofTheOrcs()
    game.play()
