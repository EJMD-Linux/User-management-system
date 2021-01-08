"""接受用户数据的输入与数据的临时存储"""

from data_handle import *


def num_input():
    """接收用户对功能的选择"""
    number = input("\n选择哪个功能：    ")

    if number == '1':
        clear()
        print("-" * 13 + "下面开始录入学生成绩：" + "-" * 13)
    elif number == '2':
        clear()
        print("-" * 13 + "下面开始显示学生成绩：" + "-" * 13)
    elif number == '3':
        clear()
        print("-" * 13 + "下面开始查询学生成绩：" + "-" * 13)
    elif number == '4':
        clear()
        print("-" * 13 + "下面开始查询学生成绩平均分：" + "-" * 13)
    elif number == '5':
        clear()
        print("-" * 13 + "下面开始查询学生成绩最高分：" + "-" * 13)
    elif number == '6':
        clear()
        print("-" * 13 + "下面开始查询学生成绩最低分：" + "-" * 13)
    elif int(number) > 6:
        clear()
        print("\n      !!!!! 输入错误数字 !!!!!\n")
    elif number == 'q':
        clear()
        print("\n" + "*" * 31 + "\n" + "    系统关闭，感谢您的使用！！" + "\n" + "*" * 31)
    return number
































































































