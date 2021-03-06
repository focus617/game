#!/usr/bin/env python
# -*- Coding：utf-8 -*-
"""
《python应用开发实战》
"""
import argparse
import random
import textwrap

from const import  LINE_WIDTH

def print_dotted_line(width=LINE_WIDTH):
    """漂亮的分割线"""
    print('-'*width)


def print_bold(msg, end='\n'):
    """用加亮的方式显示字符串"""
    print('\033[1m'+msg+'\033[0m', end=end)


def show_theme_message(width=LINE_WIDTH):
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
        '决定绕道而行。当他走进村庄时，他看见几个木屋'
        '，周围没有任何敌人。犹豫之后，他决定走进其中'
        '一间木屋......'
    )
    # 调整输出格式，以填充的形式输出
    print(textwrap.fill(msg, width=width//2))
    print_dotted_line()


# def weighted_random_selection(obj1, obj2):
#     weighted_list = 3*[id(obj1)] + 7*[id(obj2)]
#     selection = random.choice(weighted_list)
#     if selection == id(obj1):
#         return obj1
#     else:
#         return obj2


def weighted_random_selection(obj1, obj2):
    """ new version to allow non-injure to both units with 10% possibility """
    weighted_list = 4*[id(obj1)] + 5*[id(obj2)] + 1*[None]
    selection = random.choice(weighted_list)
    if selection == id(obj1):
        return obj1
    elif selection == id(obj2):
        return obj2
    else:
        return None


def process_args(args=None, namespace=None):
    """ 处理命令行参数 """
    parser = argparse.ArgumentParser(
        prog='AttackofTheOrcs',
        description="A magic game",
        epilog="This is where you might put example usage"
    )

    # subparsers
    subparsers = parser.add_subparsers(dest='function', title='游戏类型', description="可选择的游戏")
    parser_a = subparsers.add_parser('playgame', help='playgame help')
    parser_a.add_argument('-n', dest='hutnumber',  type=int, choices=[0, 1, 2, 3, 4, 5, 6, 7],
                        default=6, help='Help text for setup hut number in village')

    parser_b = subparsers.add_parser('test', help='test help')

    args = parser.parse_args(args, namespace)
    return vars(args)
