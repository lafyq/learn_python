
import pymysql


"""
这节课主要内容就是把一个数据连接对象封装，查询
"""

class MysqlSearch(object):

    def __init__(self):
        self.get_conn()

    def get_conn(self):
        """获取数据库连接"""
        try:
            self.conn = pymysql.connect(
                host='127.0.0.1',
                port=3306,
                user='root',
                passwd='123456',
                db='test',
                charset='utf8'
            )

        except pymysql.Error as e:
            print('Error: %s' % e)

    def close_conn(self):
        """关闭数据库连接"""
        try:
            if self.conn:
                self.conn.close()
        except pymysql.Error as e:
            print('Error: %s' % e)

    def get_one(self):
        """查询一条数据"""
        # 准备SQL
        sql = 'select * from `news` where `types` = %s ORDER BY `created_at` DESC '
        # 找到中间人
        cursor = self.conn.cursor()
        # 执行SQL
        cursor.execute(sql, ('百家', ))  # 注意这里传入的必须是一个tuple
        # 拿到结果
        # res = cursor.fetchone()

        # 处理数据
        print('--' * 30)
        print('cursor.description : ', cursor.description)
        print('cursor.rowcount : ', cursor.rowcount)
        print('--' * 30)

        # 将取出来的数据带上属性名称弄成一个字典，那么将来取数据就可以根据属性名称来取
        # 关于zip函数：http://www.runoob.com/python/python-func-zip.html
        res = dict(zip([k[0] for k in cursor.description], cursor.fetchone()))
        print('res ：', res)

        # 关闭游标
        cursor.close()
        # 关闭连接
        self.close_conn()

        return res


    def get_all(self):
        """查询所有符合条件数据"""
        # 准备SQL
        sql = 'select * from `news` where `types` = %s ORDER BY `created_at` DESC '
        # 找到中间人
        cursor = self.conn.cursor()
        # 执行SQL
        cursor.execute(sql, ('百家',))  # 注意这里传入的必须是一个tuple
        # 拿到结果

        # 处理数据
        res = [dict(zip([k[0] for k in cursor.description], data)) for data in cursor.fetchall()]
        # 关闭游标
        cursor.close()
        # 关闭连接
        self.close_conn()

        return res


    def add_one(self):
        """新增一条数据"""
        try:
            sql = "INSERT INTO `news`(`title`,`image`, `content`, `types`) VALUE " \
                  "('标题1', '/static/img/news/01.png', '新闻内容1', '推荐');"

            cursor = self.conn.cursor()

            cursor.execute(sql)


            self.conn.commit()  # 是连接去提交事务,没有执行提交的话数据只是在缓存中

            cursor.close()

        except:
            print('Error')
            self.conn.rollback()

        self.close_conn()

if __name__ == '__main__':
    search = MysqlSearch()
    # res = search.get_one()
    # print(res['title'])

    # res = search.get_all()
    # for item in res:
    #     print(item)

    search.add_one()



