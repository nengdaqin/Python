# 打开两个文件(源文件和复制的文件)
file_read = open("qnd.txt")
file_wirte = open("qnd.txt[大附件]", "w")

# 读写文件(读取源文件并把它写入复制的文件)
while True:
    text = file_read.readline()
    if not text:
        break
    file_wirte.write(text)

# 关闭文件(源文件和复制的文件)
file_read.close()
file_wirte.close()