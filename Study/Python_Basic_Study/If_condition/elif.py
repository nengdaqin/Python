"""
在嵌套 if 语句中，可以把 if...elif...else 结构放在另外一个 if...elif...else 结构中:
if 表达式1:
    语句
    if 表达式2:
        语句
    elif 表达式3:
        语句
    else:
        语句
elif 表达式4:
    语句
else:
    语句
"""
import random

# 定义一个变量 记录分数
# score = -100
# 通过判断分数 得到一个描述(优 良 中 差)

# score = int(input("请输入分数："))
# if score >= 90:
#     print("优秀")
# elif score <90 and score >= 80:
#     print("良好")
# elif score < 80 and score >= 70:
#     print("中")
# elif score <70 and score >= 60:
#     print("及格")
# else:
#     print("不及格")

"""
# 定义holiday_name字符串变量记录节日
# 如果是情人节，买玫瑰/看电影
# 如果是平安夜，买苹果/吃大餐
# 如果是生日，买礼物/买蛋糕
# 其他的日子，每天都是节日
"""


# holiday_name = input("请输入节日：")
# # holiday_name = "情人节"
# if holiday_name == "情人节":
#     print("买玫瑰\n看电影")
#
# elif holiday_name == "平安夜":
#     print("买苹果\n吃大餐")
#
# elif holiday_name == "生日":
#     print("买礼物\n买蛋糕")
#
# else:
#     print("每天都是节日！")


"""
#猜拳游戏
# 导入随机工具包-random
"""


# 定义一个玩家的变量
# player = int(input("请出拳：石头（0），剪刀（1），布（2）："))
#
# # 定义一个电脑的随机变量
# computer = random.randint(0, 2)
# print("玩家出的是: %d, 电脑出的是： %d" % (player, computer))
# #玩家胜利
# if ((player == 0 and computer == 1)
#         or (player == 1 and computer == 0)
#         or (player == 2 and computer == 0)):
#     print("玩家胜利！")
# #打成平局
# elif (computer == player):
#     print("打成平局")
# #玩家失败
# else:
#     print("玩家失败！")