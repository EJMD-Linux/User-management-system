# -*- coding: utf-8 -*-
# 开发人员   ：耳机没电
# 开发时间   ：2020/11/22  8:51
# 文件名称   ：c2.1.PY
# 开发工具   ：PyCharm

# from c2 import *
# fish1 = Fish1()
# fish1.show_place()
# print()
# fish1.swim('鲟鱼')
# fish1.show_place()


# 使用get方式获取数据
# import requests
# url = "http://www.cntour.cn/"
# data = requests.get(url)
# print(data.text)


# 使用post方法实现网页的部分功能
# import requests
# import json
#
# def get_translation(word):
#     url = "http://fanyi.youdao.com/translate"
#     detial = {
#         "i": word,
#         "from": "AUTO",
#         "to": "AUTO",
#         "smartresult": "dict",
#         "client": "fanyideskweb",
#         "salt": "16060067182216",
#         "sign": "15cd00bea80a6e4427406f3cc0d714da",
#         "lts": "1606006718221",
#         "bv": "cc652a2ad669c22da983a705e3bca726",
#         "doctype": "json",
#         "version": "2.1",
#         "keyfrom": "fanyi.web",
#         "action": "FY_BY_CLICKBUTTION"
#     }
#     response = requests.post(url, data=detial)
#     content = json.loads(response.text)
#     print(content['translateResult'][0][0]['tgt'])

# get_translation("耳机没电")




# content = []
# for i in range(10):
#     content.append(str(i) + " ")
# with open("E:\\py_modules\\aa.txt", "w") as f1:
#     f1.writelines(str(content))
#
# with open("E:\\py_modules\\aa.txt", "r") as f2:
#     data = f2.read()
#     print(data)



# content = []
# for i in range(10):
#     content.append(str(i) + " ")
# filename = "E:\\py_modules\\aa.txt"
# with open(filename, 'r') as f:
#     data = f.readlines()
#
# for i in data:
#     print(i)



# import sys
# sys.path.append("E:\\py_modules\\")
# from a import *
# codfish = Codfish()
# codfish.show_location()
# codfish.swim("Codfish")
# codfish.show_location()


# import json
# dict = {'a': '1', 'b': '2', 'c': '3'}
#
# json_str = json.dumps(dict)
# print(json_str)
# print(repr(dict))
# print()
#
# dict1 = json.loads(json_str)
# print(dict1)
#
# content = []
# for i in range(10):
#     content.append(str(i) + ' ')
# with open("E://py_modules//aa.txt", 'w') as f:
#     json.dump('\n' + str(content), f)
#
# with open("E://py_modules//aa.txt", 'r') as f:
#     content = f.read()
#     print(json.loads(content))


# from colorama import Fore, Back, Style, init
#
# if __name__ == "__main__":
#     init(autoreset=True)
#     print(Fore.RED + "some red words~~~")
#     print(Fore.GREEN + "some green words~~~")
#     print(Fore.BLUE + "some blue words~~~")
#     print(Back.GREEN + "with a green background")
#     print(Style.DIM + "and in dim text")
#     # print(Style.RESET_ALL)
#     print("hhhhhh")



# from datetime import datetime, timedelta
# print("now the time is:  {}".format(datetime.now()))
#
# one_day = timedelta(days=1)
# print("yesterday is:  {}".format(datetime.now() - one_day))
#
# nowtime = datetime.now()
# print('\n' + 'now try to depart the time:')
# print("year:   {}\nmonth:  {}\nday:    {}".format(nowtime.year, nowtime.month, nowtime.day))


# import os
# print(os.getcwd())


# def Test(*args, **kwargs):
#     if len(kwargs) == 0:
#         print("this function accept no data!!")
#     else:
#         print(kwargs)
#         print(args)
#
#
# test = Test('6', '6', '6', a=1, b=2, c=3)


# def a(x):
#     x = 10
#     def b(y):
#         nonlocal x
#         x += 10
#         y = x + 10
#         return y
#     return b(x)
#
#
# result = a(5)
# print(result)


# 异常处理
# a = 10
# b = 20
# try:
#     a += 10
#     b = a / ((a / b) - 1)
# except Exception as e:
#     print("something is wrong！！！")
#     print(e)
# else:
#     print("programme runs well!")
# finally:
#     for i in range(10):
#         print("EJMD-666")


# b = [2, 4, 2, 5, 2, 5, 2, 42, 4]
# b.sort()
# print(b)

# b = [2, 4, 2, 5, 2, 5, 2, 42, 4]
# b.sort(reverse=True)
# print(b)

# b = [2, 4, 2, 5, 2, 5, 2, 42, 4]
# c = sorted(b)
# print(c)


# dict = {}
# dict['a'] = 1
# dict['b'] = 2
# print(dict)
# for i in range(10):
#     for j in range(10):
#         dict[i] = str(j)
#
# print(dict)


# import random
#
# class Fish():
#     """鱼类的基类"""
#     def __init__(self):
#         self.x = 0
#         self.y = 0
#         self.z = 0
#
#     def swim(self, name):
#         print(name + " is swimming!!")
#         self.x += random.randint(1, 10)
#         self.y += random.randint(1, 10)
#         self.z += random.randint(1, 10)
#
#     def show_location(self):
#         print("x:  {}\ny:  {}\nz:  {}".format(self.x, self.y, self.z))
#
#
# class Codfish(Fish):
#     def __init__(self):
#         super().__init__()
#
#     def swim(self, name):
#         super().swim(name)
#
#     def show_location(self):
#         super().show_location()

# codfish = Codfish()
# codfish.show_location()
# codfish.swim("Codfish")
# codfish.show_location()




# student_number = input("number of students:  ")
# count = 0
# scores = []
# names = []
# score_points = []
# while count < int(student_number):
#     count += 1
#
#     name = input("enter your name:     ")
#     if name == 'q':
#         print("programme ends")
#         break
#     else:
#         names.append(name)
#     score = input("enter your score:   ")
#
#     if int(score) < 60:
#         print(name + "'s score is too low" + "\n")
#     else:
#         scores.append(score)
#         score_point = int(score) / 10 - 5
#         print("your score_point is:  %.1f" % score_point + "\n")
#         score_points.append(format(score_point, '.1f'))
#
# data = []
# print("the origin data:")
# for i in range(count):
#     print(names[i] + ':  ' + scores[i] + " -->  " + score_points[i])
#     data.append(names[i])
#     data.append(scores[i])
#     data.append(score_points[i])
#
# print()
# scores.sort()
# result = []
# for score in scores:
#     for i in range(3*count):
#         if score == data[i]:
#             result.append(data[i-1])
#             result.append(data[i])
#             result.append(data[i+1])
#
# print("the sorted number:")
# for i in range(0, count*3, 3):
#     print(result[i] + ":  " + result[i+1] + " -->  " + result[i+2])
#
#
#
#
# out_list = []
# student_number = input("students' number:   ")
# count = 0
# for i in range(int(student_number)):
#     count += 1
#     in_list = []
#
#     name = input("\ninput name:     ")
#     if name == 'q':
#         print("programme ends")
#         break
#
#     score = input("input score:   ")
#     if int(score) < 60:
#         print("the score is too low, input another student")
#         continue
#
#     in_list.append(name)
#     in_list.append(score)
#     out_list.append(in_list)
#
#
# for i in range(int(student_number)-1):
#     for j in range(int(student_number)):
#         if j > i:
#             if int(out_list[i][1]) > int(out_list[j][1]):
#                 out_list[i], out_list[j] = out_list[j], out_list[i]
#
# print(out_list)


# a = [1, 2, 3, 4]
# a.sort(reverse=True)
# b = sorted(a)
# print(tuple(b))


# 11.26.1
# count = 0
# data = []
# while True:
#     animal = input("your favourite animal:    ")
#     if animal == 'q':
#         print("programme ends")
#         break
#
#     fruit = input("your favourite fruit:     ")
#     if fruit == 'q':
#         print("programme ends")
#         break
#
#     count += 2
#     data.append(animal)
#     data.append(fruit)
#     print()
#
# print("\nhere are the animals:")
# for i in range(0, count-1, 2):
#     print(data[i])
#
# print("\nhere are the fruits:")
# for i in range(1, count, 2):
#     print(data[i])


# 11.26.2
# 法1：
# message = input("input your message:    ")
# print(message.split())

# 法2：
# message = input("input your message:    ")
# flag = message[len(message)-1]
# word = ''
# for i in range(len(message)):
#     if (message[i:i+1] != ' ') or (message[i:i+1] != flag):
#         word += message[i:i+1]
#     else:
#         print(word)
#         word = ''


# 11.26.3
# from random import randint
#
# numbers = []
# for i in range(15):
#     num = randint(1, 100)
#     numbers.append(num)
#
# print("the origin numbers:\n{}".format(numbers))
# print()
#
# for i in range(15-1):
#     for j in range(i, 15):
#         if numbers[i] < numbers[j]:
#             numbers[i], numbers[j] = numbers[j], numbers[i]
#
# print("the sorted numbers:\n{}".format(numbers))


# 11.26.4
# numbers_tuple = tuple(numbers)
# print("\nturn them into tuple:\n{}".format(numbers_tuple))


# 1.
# from random import randint
#
# dictionary = {}
# letter_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
#                'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# key_list = []
# for i in range(10):
#     key_list.append(letter_list[randint(0, 25)])    # 随机获取26个英文字母中的一个
#
# dictionary = dictionary.fromkeys(key_list, 0)    # 先把所有键存入，以便后面以键作为索引插入值
# for i in key_list:
#     dictionary[i] = randint(100, 1000)     # 生成100-1000的随机数作为值
#
# print(dictionary)


# 2.
# from random import randint
#
# with open("data.txt", 'w') as f:
#     for i in range(10):             # 设置了插入数据的行数
#         number_list = []
#         for j in range(10):         # 设置了每行的数据（每行都不同）
#             number_list.append(randint(1, 100))
#             number_list.append(" ")  # 插入一个空格作为数字之间的分隔
#         f.write(str(number_list))
#         f.write("\n")       # 插入一个换行符用作分隔行与行的数据
#
# with open("data.txt", 'r') as f:
#     for i in range(10):    # 10为行数
#         print(f.read())


# 3.
# # 使用第一题生成的字典
# import pickle
# text1 = pickle.dumps(dictionary)    # 对象序列化后以 bytes 对象返回
# print(text1)
# text2 = pickle.loads(text1)         # 反序列化后得到原来的字典
# print(text2)
#
# with open("data.txt", "wb") as f:   # 先打开文件才可以dump
#     pickle.dump(text2, f)
#     text = pickle.load(f)
#     print(text.spilt("\n"))        # 输出按照换行符分隔的文件内容



# list1 = [1, 2, 3, 4]
# list2 = [1, 2, 3, 4]
# dictionary = {}
# d = dictionary.fromkeys(list1, 0)
# print(d)     # 输出       {1: 0, 2: 0, 3: 0, 4: 0}
# for i, j in zip(list1, list2):
#     d[i] = j
#
# print(d)       # 输出     {1: 1, 2: 2, 3: 3, 4: 4}


































































