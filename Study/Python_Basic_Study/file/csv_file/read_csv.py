# coding=utf-8
"""
@Time    : 2020/11/17 14:58
@Author  : nengdaqin
@File    : read_csv.py
"""
import csv

with open('top250_02.csv', 'r', encoding="utf-8") as f:
    reader = csv.reader(f)
    # print(type(reader))

    # 读取某一行
    # result = list(reader)
    # print(result[2])

    # 读取全部
    # for row in reader:
    #     print(row)

    # 读取某列
    # for i in reader:
    #     print(i[3])