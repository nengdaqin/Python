"""
如果希望在创建对象的同时，就设置对象属性，可以对__init__进行改造
1.把希望设置的属性值，定义成__init__方法的参数
2.在方法内部使用 self.属性名 = 形参 接收外部传递的参数
3.在创建对象时，使用 类名(属性1，属性2)调用
"""
class Cat:
    """
    这是个猫类
    """
    def __init__(self, cat_name):

        # print("这是个初始化方法")
        # 定义属性：self.属性名 = 属性初始值
        # self.name = "Tom"
        self.name = cat_name

    def eat(self):

        print("%s爱吃鱼" % self.name)

    def drink(self):

        print("%s爱喝水" % self.name)

# 创建对象
tom = Cat("Tom")
# tom.name = "Tom"

tom.eat()
tom.drink()

# 再创建一个对象
lazy_cat = Cat("大懒猫")
lazy_cat.eat()
lazy_cat.drink()