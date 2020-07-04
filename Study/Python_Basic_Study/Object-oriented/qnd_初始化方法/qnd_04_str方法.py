"""
在Python中使用print输出一个 对象变量，默认情况下会输出这个变量引用的对象是由
哪个类创建的对象，以及在内存中的地址（十六进制表示）
如果希望使用print输出对象变量时，能够打印自定义的内容，可以用 __str__方法
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

    def __str__(self):

        return "这是一只%s猫 " % self.name

# 创建对象
tom = Cat("Tom")
# tom.name = "Tom"
tom.eat()
tom.drink()
print(tom)
