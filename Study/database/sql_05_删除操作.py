import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "tiger", "mysql")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# SQL 删除语句
#   删除数据表 EMPLOYEE 中 AGE 大于 20 的所有数据
sql = "DELETE FROM EMPLOYEE WHERE AGE > %s" % (20)
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 提交修改
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()

# 关闭连接
db.close()