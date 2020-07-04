"""
题目：输出 9*9 乘法口诀表。
"""


# 方法1
# def table(n):
#     m = n
#     sums = 0
#     for j in range(1, n + 1):
#         sums = m * j
#         print("%d*%d=%-2d" % (m, j, sums), end="  ")
#     print("")
#
#
# def table1():
#     for i in range(1, 10):
#         table(i)
#
#
# table1()


# 方法2
# for i in range(1, 10):
#     for j in range(1, i+1):
#         d = i * j
#         print("%d*%d=%-2d" % (i, j, d), end=" ")
#     print()


# 方法3
# row = 1
# while row <= 9:
#     col = 1
#     while col <= row:
#         print("%d*%d=%-2d" % (row, col, row*col), end= "  ")
#         col += 1
#     print("")
#     row += 1