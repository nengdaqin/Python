"""
缺省参数：定义函数时，向形参传递一个默认值的实参
# 注意事项：缺省参数必须放在形参的最后一位
"""

def print_info(name, gender=True):
    """
    :param name: 学生姓名
    :param gender: True是男生，False是女生
    :return:
    """
    gender_text = "男生"
    if not gender:

        gender_text = "女生"
    print("%s是%s" % (name, gender_text))


# 假设班上男生居多
print_info("小明")
print_info("小华")
print_info("小美", False)