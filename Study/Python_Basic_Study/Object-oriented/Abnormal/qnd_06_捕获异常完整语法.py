try:
    # 提示用户输入一个整数
    num = int(input("请输入一个整数："))

    # 使用5除以用户输入的整数
    result = 5 / num

    print(result)
except ValueError:
    print("请输入正确的整数")

except Exception as result:
    print("未知错误 %s" % result)

else:
    print("代码没有异常时执行")

finally:
    print("无论代码是否出现异常，都执行")