"""
题目：暂停一秒输出,并格式化当前时间。
"""
# 分析：使用 time 模块的 sleep() 函数。
import time


print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))

# 等待N秒
time.sleep(5)

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))

