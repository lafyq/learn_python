print()

"""  我们演示如何连接到MySQL服务器的test数据库：  """

# 导入mysql驱动
import mysql.connector

conn = mysql.connector.connect(user='root', password='', database='test')

cursor = conn.cursor()

# 创建user表：
cursor.execute('create table userTest (id varchar(20) primary key, name varchar(20))')

# 插入一行记录，注意mysql的占位符是 %s
"""  要注意的是,无论你要插入的数据是什么类型,占位符永远都要用 %s  """
cursor.execute('insert into userTest (id, name) VALUE (%s, %s)', ['1', 'Tom'])

# 通过rowcount获得插入的行数
print(cursor.rowcount)  # 1

cursor.close()

# 提交事务
conn.commit()


"""查询一下刚才插入的数据"""
cursor = conn.cursor()
cursor.execute('select * from userTest WHERE id = %s', ('1',))  # 将查询出来的东西放到本地缓冲区
values = cursor.fetchall()  # 定义一个结果集 让游标到本地缓冲区中取出剩下的所有行

print(values)

cursor.close()

conn.close()


"""
小结:

执行INSERT等操作后要调用commit()提交事务；

MySQL的SQL占位符是%s。
"""



