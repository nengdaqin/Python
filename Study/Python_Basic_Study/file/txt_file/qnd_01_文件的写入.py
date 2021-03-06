"""
r --以只读方式打开文件，文件的指针会放在文件的开头
r+ --打开一个文件用于读写。文件指针将会放在文件的开头
w --打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
w+ --打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
a --打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，
新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
a+ --打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。
文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
"""

# 以只写文件模式打开文件
f = open("qnd.txt", "w+", encoding="utf-8")
# 写入数据到文件中
f.write("hello world !!!\nhello python !!!")
# 写入数据完成后 关闭文件

f.close()



