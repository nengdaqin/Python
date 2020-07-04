def table():

    x = 1
    while x <= 9:
        # 定义一个变量 记录列数
        y = 1
        while y <= x:
            print("%d * %d = %d" % (y, x, x * y), end="\t")
            y += 1
        # 换行
        print()
        x += 1
