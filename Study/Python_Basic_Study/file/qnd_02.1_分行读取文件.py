# 以只读的文件模式打开文件
f = open("qnd.txt", "r", encoding="utf=8")
# 读取文件中的数据
while True:
    result = f.readline()
    if not result:
        break
    print(result)
# 读取完后关闭文件
f.close()


# 读取电脑的文件
# file_path = "C:/Users/qnd/Desktop/keycode.txt"
# with open(file_path, "r", encoding="utf=8") as f:
#     while True:
#         # 读取一行信息
#         file = f.readline()
#         if not file:
#             break
#     # 读取所有行(整个文件信息)
#     # file = f.readlines()
#         print(file, end=" ")