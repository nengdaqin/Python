# 1.异常：
#     程序在运行的时，如果Python解释器遇到一个错误，会停止程序运行，并提示一些错误信息
# 1.1抛出异常：
#     程序停止执行且提示错误信息这个动作，就是抛出异常


# 2.简单的异常捕获
# try:
#     # 不能确定正确执行的代码
#     num = int(input("请输入一个整数："))
# except ValueError:
#     # 报错后处理的代码
#     print("请输入正确的整数")


# while True:
#     try:
#         x = int(input("请输入一个数字: "))
#         break
#     except ValueError:
#         print("您输入的不是数字，请再次尝试输入！")

x = 10
if x > 5:
    raise Exception('x 不能大于 5。x 的值为: {}'.format(x))