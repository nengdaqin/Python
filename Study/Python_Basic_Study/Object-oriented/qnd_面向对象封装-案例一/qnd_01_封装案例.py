"""
# 封装：
#     1.封装是面对对象编程的一大特点
#     2.面向对象编程的第一步--将【属性】和【方法】封装到一个抽象的 类中
#     3.外界使用类创建对象，然后让对象调用方法
#     4.对象方法的细节都被 【封装】 在 【类的内部】

# 提示：
#     在对象的方法内部，是可以直接访问对象的属性的
"""


# 需求：
#     1.小明体重75kg
#     2.小明每次跑步减少0.5kg
#     3.小明每次吃东西增加1kg

# 分析
#     1.定义一个 person 类
#     2.name ， weight 属性
#     3.run(self)  eat(self) 方法

class Person:

    def __init__(self, name, weight):
        # self.属性名 = 形参
        self.name = name
        self.weight = weight

    def __str__(self):

        return "我的名字叫%s，体重是 %.2f kg" % (self.name, self.weight)


    def run(self):

        print("%s 爱跑步" % self.name)
        self.weight -= 0.5


    def eat(self):

        print("%s 爱吃零食" % self.name)
        self.weight += 1


# 使用person类创建对象

xiaoming = Person("小明", 75.0)

xiaoming.run()
# xiaoming.eat()
print(xiaoming)