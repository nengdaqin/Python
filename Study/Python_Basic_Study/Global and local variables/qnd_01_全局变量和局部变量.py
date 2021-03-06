"""
全局变量和局部变量
"""

# “局部变量” 是在 ‘函数内部’定义的变量，只能在函数内部使用
# “全局变量”是在 '函数外部'定义的变量（没有定义在某个函数内），所有函数内部都可以使用这个变量
# 在其他语言开发中大多 不推荐 使用全局变量--可变范围太大，导致程序不好维护

# def demo1():
#
#     num = 10
#     print("函数demo1内部的函数是 %d" % num)

# 不能调用函数内部的变量
# print("%d" %num)

# def demo2():
#
#
#     # print("%d" % num)
#     pass

# demo1()
# demo2()

"""
局部变量的生命周期：变量从创建到被系统回收的过程
局部变量在函数执行时才被创建
函数执行结束后就被系统回收
局部变量在生命周期内，可以用来存储函数内部临时使用到的数据
不同函数内部，可以定义相同名字的变量，且彼此之间不会有影响
"""


"""
全局变量
"""

num = 12

def demo3():

    # 希望修改全局变量
    # 在Python中，是不允许直接修改全局变量的值
    # 如果使用赋值语句，会在函数内部，定义一个局部变量
    num = 99
    print("demo3 ==> %d " % num)

demo3()


def demo4():

    print("demo4 ==> %d" % num)

demo4()

"""
总结：两个函数都能调用 num 变量
"""