import pymysql

# def create_table():
# 打开数据库连接
db = pymysql.connect(host="localhost", user="root", password="tiger",
                     database="game", charset="utf8")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS LOL")

# 使用预处理语句创建表
sql = """create table LOL (
    hero_name  char(20) not null,
    occupation char(20),
    home  char(20),
    types_of_attacks  char(20),
    )"""


cursor.execute(sql)


# 关闭数据库连接
db.close()

# def main():
#     create_table()
# #
# if __name__ == "__main__":
#     main()

