import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "tiger", "mysql")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# SQL 更新语句
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()

# 关闭数据库连接
db.close()