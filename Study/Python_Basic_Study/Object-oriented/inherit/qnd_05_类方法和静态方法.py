"""
5.1类属性就是针对类对象定义的属性
    使用赋值语句在class关键字下方可以定义类属性
    类属性用于记录这个类相关的特征

5.2类方法就是针对类对象定义的方法
    在类方法内部可以直接访问类属性或者调用其它类方法
语法如下：
    @classmethod
    def 类方法名(cls):
    pass
类方法需要用标识符@classmethod来标识，告诉解释器这是个类方法
类方法的第一个参数是 cls
    在类方法内部
    也可以使用.cls访问类的属性和调用其它类方法
"""

# 案例1
# class Tool(object):
#     # 使用赋值语句定义类属性，记录创建工具对象总数
#     count = 0
#     @classmethod
#     def show_tool_count(cls):
#         print("工具的总数为；%d" % cls.count)
#
#     def __init__(self, name):
#         self.name = name
#
#         # 针对类属性做计数+1
#         Tool.count += 1
#
# # 创建工具
# tool1 = Tool("f斧头")
#
# # 调用类方法
# Tool.show_tool_count()


"""
静态方法：
    如果封装的一个方法不需要访问 实例属性/实例方法 或类属性/类方法
    可以把这个方法封装成一个静态方法
语法如下
@staticmethod
def 静态方法名():
    pass
静态方法需要用修饰器@staticmethod来标识
注：调用静态方法需要用 (类名.) 调用
"""

# class Car(object):
# #
# #     @staticmethod
# #     def run():
# #         print("车在路上行驶！！")
# #
# # # 调用静态方法
# # Car.run()