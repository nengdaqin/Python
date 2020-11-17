# 导入模块
import json

# 将json对象转成字典 -> 进行解码
with open("hm.json", "r", encoding="utf-8") as f:
    # 获取文件中数据 -> 字典
    new_dict = json.load(f)

    # 查看类型
    print(type(new_dict))

    # 获取名字
    print(new_dict["name"])

    # 获取年龄
    print(new_dict["age"])

    # 获取学号
    print(new_dict["no"])
