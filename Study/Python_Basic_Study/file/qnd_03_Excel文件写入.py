# 导入模块
import xlsxwriter

# 打开student.xlsx文件
workbook = xlsxwriter.Workbook("student.xlsx")
# 创建一张工作表
worksheet = workbook.add_worksheet()
# 设置第一行信息
worksheet.write(0, 0, "学号")
worksheet.write(0, 1, "姓名")
worksheet.write(0, 2, "年龄")

# 学生信息列表
student_list = [{"name": "小明", "age": 20, "no": "20170901001"},
                {"name": "小红", "age": 21, "no": "20170901002"},
                {"name": "小刚", "age": 20, "no": "20170901003"},
                {"name": "小海", "age": 23, "no": "20170901004"},
                {"name": "小阳", "age": 25, "no": "20170901005"}]

# 遍历列表
for i, info in enumerate(student_list):
    # 写入数据
    # write(第x行, 第x列, 写入的数据)
    worksheet.write(i + 1, 0, info["no"])
    worksheet.write(i + 1, 1, info["name"])
    worksheet.write(i + 1, 2, info["age"])

# 关闭文件
workbook.close()