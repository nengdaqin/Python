"""
全局变量
"""

# num = 12
#
# def demo1():
#
#     # 如果希望修改全局变量的值，使用global关键字声明一下变量
#     # global 会告诉解释器后面的变量是一个全局变量，再使用赋值语句时，就不会创建局部变量
#     global num
#     num = 99
#
#     print("demo3 ==> %d " % num)
#
# demo1()
#
#
# def demo2():
#
#     print("demo4 ==> %d" % num)
#
# demo2()


"""
为了避免局部变量和全局变量混淆，在定义全局变量时，应在全局变量名前加 g_ 或 gl_ 的前缀
"""
g_num = 12

def demo3():

    # 如果希望修改全局变量的值，使用global关键字声明一下变量
    # global 会告诉解释器后面的变量是一个全局变量，再使用赋值语句时，就不会创建局部变量

    num = 99

    print("demo3 ==> %d " % num)

demo3()


def demo4():

    print("demo4 ==> %d" % g_num)

demo4()
