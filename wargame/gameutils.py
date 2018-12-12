#!/usr/bin/env python
# -*- Coding：utf-8 -*-
"""
《python应用开发实战》
"""

import random
import textwrap


def print_dotted_line(width=72):
    """漂亮的分割线"""
    print('-'*width)


def print_bold(msg, end='\n'):
    """用加亮的方式显示字符串"""
    print('\033[1m'+msg+'\033[0m', end=end)


def show_theme_message(width=72):
    print_dotted_line()
    # ---------------------------------------
    # 输出字体颜色格式的更改
    # 1:高亮显示，35：前景色为紫红色，34：背景色为蓝色
    # 格式为‘\033[显示方式;前景色;背景色 +'text' +'\033[0m'
    print('\033[1;35;34m'+'兽人之袭V1.0.1:'+'\033[0m')

    msg = (
        '人类和他们的敌人——兽人之间的战争即将开始。'
        'foo爵士，守卫在南部平原的勇敢骑士之一，开'
        '始了一段漫长的旅途。在一个未知的茂密的森'
        '林，他发现了一个小的孤立居住点，因为'
        '疲劳的原因，再加上希望能补充到粮食储备，他'
        '决定绕道而行。当他走进村庄时，他看见5个木屋'
        '，周围没有任何敌人。犹豫之后，他决定走进其中'
        '一间木屋......'
    )
    # 调整输出格式，以填充的形式输出
    print(textwrap.fill(msg, width=width//2))
    print_dotted_line()


def weighted_random_selection(obj1, obj2):
    weighted_list = 3*[id(obj1)] + 7*[id(obj2)]
    selection = random.choice(weighted_list)
    if selection == id(obj1):
        return obj1
    else:
        return obj2


# def weighted_random_selection(obj1, obj2):
#    """ new version to allow non-injure to both units with 10% possibility """
#     weighted_list = 3*[id(obj1)] + 6*[id(obj2)] + 1*[None]
#     selection = random.choice(weighted_list)
#     if selection == id(obj1):
#         return obj1
#     elif selection == id(obj2):
#         return obj2
#     else:
#         return None



