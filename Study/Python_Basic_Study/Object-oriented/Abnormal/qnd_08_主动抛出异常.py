def input_password():

    # 1.提示用户输入密码
    pwd = input("请输入密码：")

    # 2.判断密码的长度>=8，返回用户输入的密码
    if len(pwd) >= 8:
        return pwd

    # 3.判断密码长度<8，主动抛出异常
    # print("主动抛出异常")

    # 创建异常对象
    ex = Exception("密码长度不够")
    # 主动抛出异常
    raise ex

# 捕获异常
try:
    # 提示用户输入密码
    print(input_password())
except Exception as result:
    print(result)