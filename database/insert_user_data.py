import pymysql

conn = pymysql.connect(host="192.168.187.129", user="root", password="123456", database="litemall", port=3306)
cursor = conn.cursor()
insert_user = """INSERT INTO `litemall_user` VALUES ('{}', 'user{}', '$2a$10$lTu9qi0hr19OC800Db.eludFr0AXuJUSrMHi/iPYhKRlPFeqJxlye', '1', null, '2020-12-10 09:23:09', '192.168.187.1', '0', 'user{}', '', '', '', '', '0', '2019-04-20 22:17:43', '2020-12-10 09:23:09', '0');"""

for i in range(124, 20002):
    print(insert_user.format(i, i, i))
    cursor.execute(insert_user.format(i, i, i))
    conn.commit()
cursor.close()
conn.close()
