import pymysql

try:
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,  # 这里有坑：port = '3306'
        user='root',
        passwd='123456',  # 这里有坑：passwd = 123456
        db='test',
        charset='utf8'  # 这里有坑：charset = 'utf-8'
    )


    """
    cursor(游标)：可以将游标理解成一个中间人
    通过配置信息打开连接conn --> 准备SQL --> 通过连接信息conn找一个中间人(打开cursor) -->
     让这个中间人去执行SQL --> 从中间人那里拿到结果 --> 打发走中间人(关闭cursor) --> 关闭连接
    """
    cursor = conn.cursor()  # 获取游标
    cursor.execute('SELECT * FROM `Test`')  # 使用游标执行sql语句
    res = cursor.fetchall()  # 从缓存中获取结果集
    print(res)

except pymysql.Error as e:
    print('Error: %s' % e)
