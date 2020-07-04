"""
列表的数据统计
"""

name_list = ["Candy", "Lucy", "Kity","Candy"]
# len(length 长度)函数可以统计列表中元素的总数
list_len = len(name_list)
print("列表中包含%d的个数" % list_len)

# count-可以统计函数中某一个元素出现的次数
count = name_list.count("Candy")
print("Candy出现了 %d次" % count)


