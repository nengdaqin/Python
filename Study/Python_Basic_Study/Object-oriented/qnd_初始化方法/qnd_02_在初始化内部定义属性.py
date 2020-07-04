class Cat:
    """
    这是个猫类
    """
    def __init__(self):

        print("这是个初始化方法")
        # 定义属性：self.属性名 = 属性初始值
        self.name = "Tom"


    def eat(self):

        print("%s爱吃鱼" % self.name)

    def drink(self):

        print("%s爱喝水" % self.name)

# 创建对象
tom = Cat()
# tom.name = "Tom"

tom.eat()
tom.drink()


