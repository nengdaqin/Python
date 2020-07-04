def measure(num_list):
    """
    测量温度
    :return:返回函数中变量的值
    """
    print("开始测量...")
    # 通过在函数内部调用方法修改可变参数
    num_list.append(4)
    print(num_list)

    print("测量结束...")

gl_list = [1, 2, 3]
measure(gl_list)
print(gl_list)
# gl_id = id(gl_list)
# print(gl_id)