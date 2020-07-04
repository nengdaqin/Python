"""
元组的基本使用
"""
# my_tuple = ("Candy", 18, 1.65, 18)

# 取值和取索引
# print(my_tuple[0])
# print(my_tuple.index(18))

# # 统计计数
# print(my_tuple.count(18))

# 统计元素个数
# print(len(my_tuple))

# 用for循环遍历元组(由于元组存储的是不同类型的数据，所以不好遍历)
# my_tuple = ("Candy", 18, 1.65)
# for info_tuple in my_tuple:
#     print("名字是 %s  年龄是 %d  身高是 %.2f " % (my_tuple))

"""
元组的应用场景
"""
# 1.函数的参数和返回值，一个函数可以接收任意多个参数，或者一次返回多个数据
# 2.格式化字符串，格式化字符串后面的（）本质上就是一个元组
# 3.让列表不可被修改，已保证数据的安全

# 格式化字符串

# my_tuple = ("Candy", 18, 1.65)
# print("名字是 %s  年龄是 %d  身高是 %.2f " % (my_tuple))
# print("名字是 %s  年龄是 %d  身高是 %.2f " % ("Candy",18,1.65))
# info_str = "名字是 %s  年龄是 %d  身高是 %.2f " % my_tuple
# print(info_str)


"""
元组与列表的转换
"""
# 使用list可以将元组转换成列表
my_tuple = ("Candy", 18, 1.65)
# list[元组]
my_list = list[my_tuple]

# 使用tuple可以将列表转换成元组
# tuple(列表)
my_tuple = tuple(my_list)
