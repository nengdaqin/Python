# coding=utf-8
"""
@Time    : 2020/11/17 14:30
@Author  : nengdaqin
@File    : read_yaml_file.py
"""
import yaml
file_1 = open("config.yml")
# 返回一个字典
yml = yaml.load(file_1, Loader=yaml.FullLoader)
print(yml)
print(type(yml))
#
# file = {"name": "Jack", "age": 23, "children": {"name": "Jason", "age": 2, "name1": "jeff", "age_1": 4}}
#
# # yml = yaml.dump()
# print(yaml.dump(file,))
# print(type(yml))
