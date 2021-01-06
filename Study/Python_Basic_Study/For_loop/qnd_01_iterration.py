"""
循环遍历
"""

# 遍历：就是从头到尾 依次的从列表获取数据
# 在循环体内部针对每个元素，执行相同的操作

# for循环
# for name(自定义) in name_list(列表名)
# 循环内部针对列表元素进行操作
# print（name）

"""完整的for循环"""

for num in [1, 2, 3]:
    print(num)
    if num == 2:
        break
    # 如果循环体内部使用了break退出循环，则下方else的代码不会执行
else:
    print("代码会执行吗")

# student = [
#     {"name": "小米"},
#     {"name": "小美"}
# ]
# for stu_dict in student:
#     # print(stu_dict)
#     find_name = "小花"
#     if find_name == "小米":
#         print("找到了 %s" %(find_name))
#         # 如果已经找到了，退出循环，不再执行后面代码
#         break
# else:
#     print("抱歉，没找到 %s" % (find_name))


# num = 0
# for i in range(1, 101):
#     num += i
# print(num)

result = 0
num = 0
while num <= 100:
    print(num)
    result += num
    num += 1
print(result)