class Cat:
    """
    这是个猫类
    """
    def eat(self):

        print("%s爱吃鱼" % self.name)

    def drink(self):

        print("%s爱喝水" % self.name)

# 创建对象
tom = Cat()
# tom.name = "Tom"

tom.eat()
tom.drink()

# 如果在运行时，没有找到name，那么程序会报错
tom.name = "Tom"


