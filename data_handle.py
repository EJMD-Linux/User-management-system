"""用于实现各种小功能"""
from fun_realize import *
import os


def clear():
    """定义dos中的清屏方法，清除已输出的内容"""
    os.system('cls')


def goto_fun(number):
    """根据输入的序号去执行不同的函数"""
    if str(number) == '1':
        input_scores()
    elif str(number) == '2':
        show_scores()
    elif str(number) == '3':
        select_scores()
    elif str(number) == '4':
        select_average()
    elif str(number) == '5':
        select_max()
    elif str(number) == '6':
        select_min()

































