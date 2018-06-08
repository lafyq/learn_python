print()
"""
表是数据库中存放关系数据的集合，一个数据库里面通常都包含多个表，
比如学生的表，班级的表，学校的表，等等。表和表之间通过外键关联。

** 要操作关系数据库，首先需要连接到数据库，一个数据库连接称为Connection；

** 连接到数据库后，需要打开游标，称之为Cursor，通过Cursor执行SQL语句，然后，获得执行结果。


下面以sqlite演示

SQLite是一种嵌入式数据库，它的数据库就是一个文件。由于SQLite本身是C写的，而且体积很小，
所以，经常被集成到各种应用程序中，甚至在iOS和Android的App中都可以集成。

Python就内置了SQLite3，所以，在Python中使用SQLite，不需要安装任何东西，直接使用。
"""

import sqlite3

# 连接到SQLite数据库
# 数据库文件是 test.db （如果文件不存在，会在当前目录创建）
conn = sqlite3.connect('test.db')

# 创建一个 cursor (游标)
cursor = conn.cursor()

# 执行一条sql语句：创建user表
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')

# 继续执行一条SQL语句，插入一条记录:
cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')

# 通过rowcount获得插入的行数
print(cursor.rowcount)  # 1

# 关闭cursor
cursor.close()

# 提交事务
conn.commit()

# 关闭connection
conn.close()

"""  我们再试试查询记录： """

# 连接到数据库
conn = sqlite3.connect('test.db')

# 打开cursor
cursor = conn.cursor()

# 执行查询语句
cursor.execute('select * from USER WHERE id=?', ('1', ))  # 将查询出来的东西放到本地缓冲区

# 获得查询结果集
values = cursor.fetchall()  # 定义一个结果集 让游标到本地缓冲区中取出剩下的所有行

print(values)

# 关闭cursor
cursor.close()

# 关闭connection
conn.close()

"""
使用Python的DB-API时，只要搞清楚Connection和Cursor对象，打开后一定记得关闭，就可以放心地使用。

使用Cursor对象执行insert，update，delete语句时，执行结果由rowcount返回影响的行数，就可以拿到执行结果。

使用Cursor对象执行select语句时，通过featchall()可以拿到结果集。
    返回二维元组，如(('id','title'),('id','title')...),

如果SQL语句带有参数，那么需要把参数按照位置传递给execute()方法，有几个?占位符就必须对应几个参数，
比如说：cursor.execute('select * from user where name=? and pwd=?', ('abc', 'password'))
    ps.后面传进去的是一个tuple(元组)，单个参数时要这样传：cursor.execute('sql...', ('abc', ))

小结：
在Python中操作数据库时，要先导入数据库对应的驱动，然后，通过Connection对象和Cursor对象操作数据。

要确保打开的Connection对象和Cursor对象都正确地被关闭，否则，资源就会泄露。

操作数据库的大概步骤： 连接到数据库conn --> 利用conn创建cursor（游标） --> 利用cursor执行SQL语句
    --> 从本地缓存中取出结果集  --> 关闭cursor（游标） --> 关闭连接conn
"""