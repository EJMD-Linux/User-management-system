"""主函数，用于调用其它功能"""

import data_show
import data_handle
import data_input

# 显示初始界面
data_show.start_interface()

# 接受到用户选择后清空界面上已有输出
# 给出提示信息与保存用户选择
number = data_input.num_input()

# 根据选择执行相应的功能
data_handle.goto_fun(number)

while True:
    goon = input("\n需要继续使用其它功能吗 (y/n)：     ")
    if goon == 'y':
        data_handle.clear()
        data_show.start_interface()
        number = data_input.num_input()
        data_handle.goto_fun(number)
    else:
        print("\n" + "*" * 31 + "\n" + "    系统关闭，感谢您的使用！！" + "\n" + "*" * 31 + "\n")
        break




























































































