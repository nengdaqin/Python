"""
f.read([count]) 读出文件，如果有count，则读出count个字节,如果不设count则读取整个文件。
f.readline ()读出一行信息。
f.readlines() 读出所有行，也就是读出整个文件的信息--读取数据为list类型，而且会把换行符读入
"""
import os
import time
# import numpy

# 以只读的文件模式打开文件
# f = open("qnd.txt", "r", encoding="utf=8")
# # 读取文件中的数据
# result = f.read()
# print(result)
# # 读取完后关闭文件
# f.close()

# 通过此方式打开文件，不需要关闭
# # as 是给文件起了个别名
# with open("qnd.txt", "r", encoding="utf=8") as q:
#     # 读取文件中的数据
#     result = q.read()
#     print(result)

# 读取电脑的文件
file_path = "C:/Users/qnd/Desktop/keycode.txt"
with open(file_path, "r", encoding="utf=8") as f:
    # 读取一行信息
    # file = f.readline()
    # 读取所有行(整个文件信息)
    file = f.readlines()
print(file)

# 批量读取文件
# cp = os.getcwd()
# print(cp)
# filelist = os.listdir()
# print(filelist)

