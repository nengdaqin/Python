my_list = ["Candy", "Lucy", "Kity"]

"""1.取值和取索引"""
# print(my_list[0])
# 知道数据的内容，想知道数据在列表中的位置(取索引)
# print(my_list.index("Lucy"))

"""2.修改"""
# my_list[0] = "Lili"

"""3.删除"""
# clear方法可以清空列表
# my_list.clear()

# remove方法可以从列表中删除指定的数据(有两个相同元素的情况下默认删除第一个)
# my_list.remove("Candy")

# pop方法默认删除列表中的最后一个元素
# my_list.pop()

# pop方法可以指定删除列表中的索引
# my_list.pop(0)

"""4.增加"""
# append在列表末尾追加数据
# my_list.append("David")

# insert在指定索引中插入数据
# my_list.insert(3,"Katie")

# extend可以把其他列表中的完整内容，追加到当前列表
# name_list = ["wang", "li", "qin"]
# my_list.extend(name_list)

"""
5.del关键字本质是将一个变量从内存中把数据删除
注意：如果使用del关键字将变量从内存中删除，
后续的代码就不能使用这个变量了
# 删除变量时，建议使用python提供的方法
"""
# name = "Candy"
# del name
# print(name)

# print(my_list)