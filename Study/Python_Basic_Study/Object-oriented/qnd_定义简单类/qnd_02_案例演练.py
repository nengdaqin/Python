"""
第一个面向对象编程
"""
# 需求：
#     小猫爱吃鱼，小猫爱喝水
# 分析：
#     定义一个猫类Cat
#     定义两个方法 eat 和 drink
#     按照需求不需要定义属性

# 定义类
class Cat:
    """
    这是个猫类
    """
    def eat(self):

        print("小猫爱吃鱼")

    def drink(self):

        print("小猫爱喝水")

# 创建对象
tom = Cat()

tom.eat()
tom.drink()

# 打印对象内存地址
# %d:可以以10进制输出
# %x：可以以16进制输出
print(tom)
addr = id(tom)
print("%x" % addr)