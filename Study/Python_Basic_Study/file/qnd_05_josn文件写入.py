# 导入模块
import json

# 定义一个字典
my_dict = {"name": "小明", "age": 23, "no": "007"}

# 将字典转成json -> 进行编码
json_str = json.dumps(my_dict)

# 打印json字符串
print(type(json_str))

# 把json数据写入到文件中
with open("hm.json", "w", encoding="utf-8") as f:
    f.write(json_str)