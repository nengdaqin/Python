"""
*
**
***
****
*****
"""

# 考虑第一件事情 分析如何打印出5行
# 定义一个变量

# row = 1
# while row <= 5:
#     col = 1
#     while col <= row :
#         print("*", end="")
#         col += 1
#
#
#     print("")
#     row += 1
"""
打印九九乘法口诀
"""
# row = 1
# while row <= 9:
#     col = 1
#     while col <= row :
#         print("%d * %d = %-2d" %(row,col,row*col) ,end="  ")
#         col += 1
#
#
#     print()
#     row += 1


"""定义一个变量 记录行数
# x = 1
# while x <= 9:
#     print(x)
#     x += 1

# 定义一个变量 记录列数
# y = 1
# while y <= 5:
#     print(y, end="  ")
#     y += 1


# 定义一个变量 记录行数
# %2d 显示两位 如果只有一位 使用空格占位 默认为右对齐
# 如果左对齐 就是 %-2d
"""
# x = 1
# while x <= 9:
#     # 定义一个变量 记录列数
#     y = 1
#     while y <= x:
#         print("%d * %d = %d" % (y, x, x * y), end="\t")
#         y += 1
#     # 换行
#     print()
#     x += 1