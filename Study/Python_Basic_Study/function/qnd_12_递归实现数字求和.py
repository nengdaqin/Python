# 定义一个函数sum_numbers
# 能够接收一个sum的整数参数
# 计算1+2+...num 的结果

def sum_numbers(num):

    # 1.设置出口
    if num == 1:
        return 1

    # 2.数字的累加num +(1..num -1)

    # 假设sum_numbers 能够正确处理1...num - 1
    temp = sum_numbers(num - 1)

    # 两个数字相加
    return temp + num

result = sum_numbers(100)
print(result)