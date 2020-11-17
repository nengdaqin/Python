# 打开两个文件(源文件和复制的文件)
file_read = open("qnd.txt")
file_wirte = open("qnd.txt[附件]", "w")

# 读写文件(读取源文件并把它写入复制的文件)
text = file_read.read()
file_wirte.write(text)

# 关闭文件(源文件和复制的文件)
file_read.close()
file_wirte.close()