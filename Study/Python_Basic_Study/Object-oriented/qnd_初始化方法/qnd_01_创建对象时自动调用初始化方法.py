"""
__init__方法:
专门用来定义一个类具有哪些属性的方法
"""
class Cat:

    def __init__(self):

        print("这是个初始化方法")

# 使用类名()创建对象时，会自动调用初始化方法 __init__
tom = Cat()