"""
#在类的外部增加类的属性

使用self在方法内部输出每只猫的名字
由哪个对象调用的方法，方法内的self 就是哪个对象的引用
在类封装的方法内部，self表示当前调用方法的对象自己
"""

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
tom.name = "Tom"

tom.eat()
tom.drink()

# 再创建一个对象

lazy_cat = Cat()
lazy_cat.name = "大懒猫"

lazy_cat.eat()
lazy_cat.drink()
