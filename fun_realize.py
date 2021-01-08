"""用于对输入数据的存储"""

import json


def input_scores():
    """实现接收数据与存储"""
    names = []
    scores = []
    data = {}

    print(" " * 4 + "-" * 6 + "enter 'q' to leave" + "-" * 6 + "\n")
    while True:
        name = input("\ninput name:     ")
        if name == 'q':
            print("------退出成绩录入------")
            break

        score = input("input score:    ")
        if score == 'q':
            print("\n------退出成绩录入------")
            break

        names.append(name)
        scores.append(score)

    data = data.fromkeys(names, 0)
    for i, j in zip(names, scores):
        data[i] = int(j)

    with open("data.txt", "w") as f:
        json.dump(data, f)


def show_scores():
    """显示存入文件的数据"""
    with open("data.txt", "r+") as f:
        data = f.read()
        data = json.loads(data)
        data = dict(data)
        names = []
        scores = []
        for i, j in zip(data.keys(), data.values()):
            names.append(i)
            scores.append(j)

        for i in range(len(names)):
            print("name:     {}\nscore:    {}\n".format(names[i], scores[i]))


def select_scores():
    """用于查询所需数据"""
    select_way = input("\n提供两种查询方式 ---- 1.按名字查询 ---- 2.按成绩查询:    ")
    if select_way == '1':
        with open("data.txt", "r+") as f:
            data = f.read()

        data = json.loads(data)
        data = dict(data)
        name = input("\nwhich name:     ")
        print()
        if name not in data.keys():
            print("--------查询无果--------")
            return None

        for i, j in zip(data.keys(), data.values()):
            if name == i:
                print("name:     {}\nscore:    {}\n".format(i, j))

    else:
        with open("data.txt", "r+") as f:
            data = f.read()

        data = json.loads(data)
        data = dict(data)
        score = input("\nwhich score:    ")
        print()
        if int(score) not in data.values():
            print("--------查询无果--------\n")
            return None

        for i, j in zip(data.keys(), data.values()):
            if int(score) == int(j):
                print("name:     {}\nscore:    {}\n".format(i, j))


def select_average():
    """确定范围内或全部成绩的平均分"""
    with open("data.txt", "r+") as f:
        data = f.read()

    data = json.loads(data)
    data = dict(data)
    judge = input("\nset range or not (1.yes   2.no):       ")
    if judge == '1':
        scores = []
        while True:
            name = input("\nname:     ")
            if name == 'q':
                break
            else:
                for i, j in zip(data.keys(), data.values()):
                    if i == name:
                        scores.append(j)

        sum_score = 0
        count = 0
        for i in scores:
            sum_score += i
            count += 1

        print("\n选定学生的平均成绩是：    %.2f" % (sum_score/count))

    else:
        sum_score = 0
        count = 0
        for i in data.values():
            sum_score += int(i)
            count += 1

        print("\n全部学生的平均成绩是：    %.2f\n" % (sum_score / count))
        print("*" * 35)


def select_max():
    """找出最高分与之对应的姓名"""
    with open("data.txt", "r+") as f:
        data = f.read()

    data = json.loads(data)
    data = dict(data)
    judge = input("\nset range or not (1.yes   2.no):       ")
    if judge == '1':
        names = []
        scores = []
        while True:
            name = input("name:     ")
            if name == 'q':
                break
            else:
                for i, j in zip(data.keys(), data.values()):
                    if i == name:
                        names.append(i)
                        scores.append(j)

        dictionary = {}
        d = dictionary.fromkeys(names, 0)
        for i, j in zip(d.keys(), scores):
            d[i] = j

        highest = (sorted(d.values(), reverse=True))[0]
        print("\n最高分有以下同学：")
        for i, j in zip(data.keys(), data.values()):
            if j == highest:
                print("\nname:     {}\nscore:    {}\n".format(i, j))

    else:
        highest = sorted(data.values(), reverse=True)[0]
        print("\n最高分有以下同学：")
        for i, j in zip(data.keys(), data.values()):
            if j == highest:
                print("\nname:     {}\nscore:    {}\n".format(i, j))


def select_min():
    """找出最低分与之对应的姓名"""
    with open("data.txt", "r+") as f:
        data = f.read()

    data = json.loads(data)
    data = dict(data)
    judge = input("\nset range or not (1.yes   2.no):       ")
    if judge == '1':
        names = []
        scores = []
        while True:
            name = input("name:     ")
            if name == 'q':
                break
            else:
                for i, j in zip(data.keys(), data.values()):
                    if i == name:
                        names.append(i)
                        scores.append(j)

        dictionary = {}
        d = dictionary.fromkeys(names, 0)
        for i, j in zip(d.keys(), scores):
            d[i] = j

        lowest = (sorted(d.values()))[0]
        print("\n最低分有以下同学：")
        for i, j in zip(data.keys(), data.values()):
            if j == lowest:
                print("\nname:     {}\nscore:    {}\n".format(i, j))

    else:
        lowest = sorted(data.values())[0]
        print("\n最低分有以下同学：")
        for i, j in zip(data.keys(), data.values()):
            if j == lowest:
                print("\nname:     {}\nscore:    {}\n".format(i, j))




















