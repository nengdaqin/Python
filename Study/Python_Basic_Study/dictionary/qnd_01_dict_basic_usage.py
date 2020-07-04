"""
字典的基本使用

# 字典的定义
# 1.dictionary（字典）是除了列表以外python中最灵活的数据类型
# 2.字典同样可以用来储存多个数据
# 3.字典和列表的区别
#   列表是有序的对象集合
#   字典是无序的对象集合
# 4.字典用{}定义       (键必须是唯一的)
#    字典使用键值对存储数据
#       键key是索引
#       值vlue是数据
#         键和值之间用 ：分隔
#         值可以是任何数据类型，但键只能使用字符串、数字或元组
"""
# Candy_dict = {"name": "Candy", "height": 1.75}

# 1.访问字典中的值
# print(Candy_dict["height"])

# 2.增加/修改(如果key存在则修改已存在的键值对，如果key不存在则新增键值对)
# Candy_dict["height"] = 165
# Candy_dict["name"] = "Kite"

# 3.删除(括号内传入的是key，而不是索引)
# Candy_dict.pop("name")

# print(Candy_dict)


# 字典的统计
# Candy_dict = {"name": "Candy", "height": 1.75, "age": 18}
# print(len(Candy_dict))

# 合并字典(如果被合并的字典中包含已存在键值对，则合并后会覆盖已有的键值对)
# age_dict = {"age": 20}
# Candy_dict.update(age_dict)

# 字典清空
# Candy_dict.clear()
# 
# print(Candy_dict)