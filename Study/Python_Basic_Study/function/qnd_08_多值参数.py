# 定义支持多值参数的函数
# 参数前加一个* 可以接收元祖
# 参数前加两个* 可以接收字典

# 一般给多值参数命名时，多使用

# *args--存放元祖参数
# **kwargs--存放字典参数



def demo(num, *args, **kwargs):

    print(num)
    print(args)
    print(kwargs)

demo(1, 2, 3, 4, age=18, name="小米")
