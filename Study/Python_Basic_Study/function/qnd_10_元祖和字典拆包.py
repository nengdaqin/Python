def demo(*args, **kwargs):

    print(args)
    print(kwargs)

# 元祖变量/字典变量
gl_nums = (1, 2, 3)
gl_list = {"name": "小米", "age": 18}

# demo(gl_nums, gl_list)

# 拆包语法，简化元祖变量/字典变量的传递
# demo(1, 2, 3, name="小米", age=18)
demo(*gl_nums, **gl_list)
