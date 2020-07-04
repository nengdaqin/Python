"""
在开发中，可以在主程序添加异常捕获
"""

def my_func1():
    print(num)

def my_func2():
    my_func1()

def my_func3():
    my_func2()

try:
    my_func3()
except Exception as a:
    print("未知异常 %s" % a)





