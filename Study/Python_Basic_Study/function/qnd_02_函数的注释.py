"""
在函数的下方，连续使用三对单引号说明
Chrl + Q 可以查看函数说明的信息
定义函数时，函数上方应空出两行
"""


def table():
    """ 打印九九乘法表"""
    x = 1
    while x <= 9:
        # 定义一个变量 记录列数
        y = 1
        while y <= x:
            print("%d * %d = %d" % (y, x, x * y), end="\t")
            y += 1
        # 换行
        print()
        x += 1


table()
