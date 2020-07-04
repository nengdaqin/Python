# 需求
#     1.房子(House)有户型、总面积和家具名称列表(新房子没有任何家具)
#     2.家具(HouseItem)有名字 和 占地面积其中
#     床(bed) 占地4平米
#     衣柜(chest)占地2平米
#     餐桌(table)占地1.5平米
#     3.将以上三件家具添加到 房子中
#     4.打印房子时，要求输出：户型、总面积、剩余面积、家具名称列表

# 剩余面积
#     1.在创建房子对象时，定义一个 剩余面积的属性、初始值和总面积相等
#     2.当调用add_item方法，向房间添加家具时， 让剩余面积-= 家具面积

# 应该先开发哪一类
#     --家具类
#     1.家具简单
#     2.房子要用到家具，被使用的类 通常先开发

"""
# HouseItem
#     name
#     area
#     __init__(self, name, area)
#     __str__(self):
"""

"""
# House
#     house_type
#     area
#     free_area
#     item_list
#     --init__(self, house_type, area)
#     __str__(self):
#     add_item(self, item):
"""