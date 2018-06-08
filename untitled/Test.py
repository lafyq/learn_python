import pymysql.cursors

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,  # 这里有坑：port = '3306'
    user='root',
    passwd='123456',  # 这里有坑：passwd = 123456
    db='test',
    charset='utf8'  # 这里有坑：charset = 'utf-8'
)

# 获取游标
cursor = conn.cursor()

# 插入数据
cursor.execute('insert into Test (t_id, t_name) VALUES (4, "大东")')

conn.commit()

# 查询数据
cursor.execute('select * from Test')
res = cursor.fetchall()

for i in res:
    print(i)
