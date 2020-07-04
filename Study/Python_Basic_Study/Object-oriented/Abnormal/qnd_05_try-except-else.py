try:
    open("hm.txt", "r")

except:
    # try中的代码发生了异常执行except代码
    print("except")
else:
    # 如果try中的代码没有发生异常 就会执行else中的代码
    print("else")