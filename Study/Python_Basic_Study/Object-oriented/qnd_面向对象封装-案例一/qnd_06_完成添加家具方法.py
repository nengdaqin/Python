class HouseItem:

    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):

        return "%s 占地 %.2f" % (self.name, self.area)

class House:

    def __init__(self, house_type, area):

        self.house_type = house_type
        self.area = area
        # 剩余面积
        self.free_area = area
        # 家具名称列表
        self.item_list = []

    def __str__(self):

        # Python能够自动将一对括号内部的代码连一起
        return ("户型：%s\n 总面积：%.2f\n [剩余面积：%.2f]\n 家具列表：%s"
                % (self.house_type, self.area, self.free_area, self.item_list))

    def add_item(self, item):
        """
        :param item: 要添加的家具
        """
        print("要添加的 %s" % item)

        # 1.判断家具面积
        if item.area > self.free_area:
            print("%s 的面积太大了，无法添加"% item.name)

            return

        # 2.将家具添加到家具列表
        self.item_list.append(item.name)

        # 3.计算房子剩余的面积
        self.free_area -= item.area

# 1.创建家具
bed = HouseItem("床", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.5)

# print(bed)
# print(chest)
# print(table)

# 2.创建房子
my_house = House("三房两厅", 90)
my_house.add_item(bed)
my_house.add_item(chest)
my_house.add_item(table)

print(my_house)

"""
小结：
    1.主程序只负责创建 房子对象和 家具对象
    2.让房子对象调用add_item方法将家具添加到家具列表
    3.面积计算、剩余面积、家具列表、等处理都被封装 到房子的内部
    
"""