"""
单例设计模式
    为了可重用代码，让代码更容易被他人理解，保证代码的可靠性
目的：
    让类创建对象，在系统中，只有唯一的一个实例
    每一次执行 类名() 返回的对象，内存地址都是相同的
"""

# ======================================================
"""
# __new__方法
#     1.使用类名创建对象时，Python的解释器首先会调用__new__方法为对象分配空间
#     2.__new__是一个由object基类提供的内置静态方法，主要作用有两个
#         (1):在内存在为对象分配空间
#         (2):返回对象的引用
# 3.Python解释器获得对象引用后，将引用作为第一个参数，传递给__init__方法
"""


# 重写__new__方法
# 1.重写__new__方法一定要 return super().__new__(cls),否则Python解释器得不到分配空间的 对象引用
# 就不会调用对象的初始化方法
# 2.注意 __new__方法的静态方法 ，在调用时需要主动传递 cls 参数

# class MusicPlayer(object):
#     def __new__(cls, *args, **kwargs):
#         # 1.创建对象时，new方法会被自动调用
#         print("创建对象，分配空间")
#         # 2.为对象分配空间
#         instance = super().__new__(cls)
#         # 3.返回对象引用
#         return instance
#
#     def __init__(self):
#         print("播放器初始化")
#
# # 创建播放器对象
# player = MusicPlayer()
# print(player)


# 单例模式 在程序中这个类创建出来的对象 只有一个(也就是占用一份内存地址)
# 单例模式 也只会走一次__init__方法(保证这个单例对象的属性也是唯一的)(name=小明 age=20)
# 合理的使用内存(避免内存浪费)
class Person(object):
    # 定义一个类属性  保存这个类创建的对象
    __instance = None
    # 定义一个类属性 判断是否是第一次走init方法
    __is_first = True

    # 创建对象
    # 重写new方法 是为了完成单例模式中的对象地址唯一
    def __new__(cls, *args, **kwargs):
        # 判断是否通过这个类创建过对象
        # 如果没有值需要创建
        if not cls.__instance:
            # 创建对象保存起来
            cls.__instance = object.__new__(cls)

        # 如果有值直接返回
        return cls.__instance

    def __init__(self, name, age):
        # 判断是否是第一次
        if Person.__is_first:
            # 赋值一次
            self.name = name
            self.age = age
            # 设置类属性is_first 为False
            Person.__is_first = False

    # def make(self):
    #
    #     hm = HMTest()
    #     hm.my_func(20, 30)


# 创建对象
xiaoming = Person("小明", 20)
print(xiaoming.name)
xiaohong = Person("小红", 21)
print(xiaohong.name)
xiaoyang = Person("小阳", 22)
print(xiaoyang.name)
#
print(xiaoming.name, xiaohong.name, xiaoyang.name)


# num = None
# # 如果不为none 也就是真
# if not num:
#     print("测试")


# 单例的好处???
class HMTest(object):
    def my_func(self, a, b):
        return a + b

# 在程序中 需要计算多次求和操作 比如1000次 可以省掉999分内存
# 每次使用
# 实例化一个对象
# hm = HMTest()
# hm.my_func(10, 20)

# 为了节约内存
