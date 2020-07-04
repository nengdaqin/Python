def measure():
    """
    测量温度
    :return:返回函数中变量的值
    """
    print("开始测量...")
    temp = 36
    wetness = 50
    tip = 39
    print("测量结束...")

    # 元祖-可以包含多个数据，因此可以使用元祖让函数一次返回多个值
    # 如果函数返回的类型是元祖，小括号可以省略
    # return （temp, wetness）
    return temp, wetness, tip
#
# result = measure()
#
# print(result)

# 如果函数返回的类型是多个元祖，同时希望单独的处理元祖中的元素
# 可以使用多个变量，一次性接收函数返回的结果
# 注意使用多个变量接收结果时，变量的个数应该和元祖中的元素的个数保持一致
gl_temp, gl_wetness, gl_tip = measure()

print(gl_temp)
print(gl_wetness)
print(gl_tip)