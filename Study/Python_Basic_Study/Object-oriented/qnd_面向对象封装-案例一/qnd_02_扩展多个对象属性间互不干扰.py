# 需求：
#     小明和小美都爱跑步
#     1.小明体重75.0kg，小美体重45.0kg
#     2.每次跑步减少0.5kg
#     3.每次吃东西增加1kg

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
xiaoming.eat()
print(xiaoming)

xiaomei = Person("小美", 45.0)
xiaomei.run()
# xiaomei.eat()
print(xiaomei)


# 同一个类创建的多个对象之间的属性 互不干扰