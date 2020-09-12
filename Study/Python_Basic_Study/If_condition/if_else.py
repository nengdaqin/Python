"""
if 判断条件:
    如果判断条件成立(True)执行的代码01
    如果判断条件成立(True)执行的代码02
    如果判断条件成立(True)执行的代码03
    ...
else:
    如果判断条件不成立(False)执行的代码01
    如果判断条件不成立(False)执行的代码02
    如果判断条件不成立(False)执行的代码03
    ...
"""

# 模拟进入网吧，请输入你的年龄，年龄大于等于18岁可以进入
# if-else嵌套：
# myage = int(input("请输入你的年龄:"))
# if myage >= 18:
#     print("可以进入网吧")
#     my_money = int(input("请输入卡上余额:"))
#     if my_money > 0 :
#         print("可以上网")
#     else:
#         print("请充值")
# else:
#     print("未满18岁，禁止进入")


# 模拟发工资流程
# if 发工资
#     print("先还信用卡")
#     if 工资还有剩余：
#         print("又可以happy了")
#     else:
#         print("噢 no，继续等30天")
# else:
#     print("继续等发工资")


# #定义一个变量记录是否发工资:
# wages = int(input("请输入是否发工资: 发工资（1），不发工资（0）:"))
# #如果发工资为True：
# if wages:
#     print("先还信用卡")
#     #再定义一个变量记录工资余额：
#     balance = int(input("请输入工资余额:"))
#     if balance >= 2000:
#         print("又可以happy了，O(∩_∩)O")
#     else:
#         print("噢no，还等30天")
# else:
#     print("继续等发工资")


"""【if嵌套】
"""

# """
# # 伪代码
# 模拟进入火车站
#     - 安检 是否有危险品
#         - 如果没有危险品 -> 可以进入火车站
#             - 判断车票 是否有车票
#                 - 如果有车票 -> 可以上火车
#                 - 如果没有火车站 -> 请买火车票
#         - 如果有危险品 -> 不可以进入火车站
#
# """
# 定义一个变量，判断是否有危险品，True表示没有危险品，False表示有危险品

# flag = True
#
# if flag:
#     print("没有危险品，可以进火车站")
#     #判断是否有车票
#     ticket = int(input("请输入车票的数量："))
#     if ticket >= 1:
#         #如果有票，可以上车
#         print("可以去乘车")
#     else:
#         #如果没票
#         print("请购买车票")
# else:
#     print("有危险品，不可以进火车站")


"""情节描述：上公交车，并且可以有座位坐下

要求：输入公交卡当前的余额，只要超过2元，就可以上公交车；如果车上有空座位，就可以坐下。

定义一个变量记录用户输入
"""
# money = int(input("请输入卡上余额："))
# #判断卡上余额：
# if money >= 2:
#     print("可以上车！")
#     # 判断是否有空座：
#     seat = True
#     if seat:
#         print("可以坐下！")
#     else:
#         print("站一会吧！")
# else:
#     print("请先去充值。")


