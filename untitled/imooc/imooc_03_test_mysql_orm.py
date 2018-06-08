from sqlalchemy import MetaData
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean


# Python3 暂时不支持MySQLdb，所以要在下面 +pymysql，不然会报错
engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/test?charset=utf8")

Base = declarative_base()

Session = sessionmaker(bind=engine)


class News(Base):
    """新闻类型"""
    __tablename__ = 'news_test'
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(String(2000), nullable=False)
    types = Column(String(10), nullable=False)
    image = Column(String(300))
    author = Column(String(20))
    view_count = Column(Integer)
    created_at = Column(DateTime)
    is_valid = Column(Boolean)

Base.metadata.create_all(engine)  # 创建数据库表



class orm(object):
    def __init__(self):
        self.session = Session()  # 这里有坑：self.session = Session

    def add_one(self):
        new_obj = News(
            title='orm标题',
            content='测试',
            types='1'
        )

        self.session.add(new_obj)
        self.session.commit()
        return new_obj

    def get_one(self):
        """查询一条数据"""
        return self.session.query(News).get(2)  # 查询id为2的元组

    def get_more(self):
        """按条件查询多条数据"""
        return self.session.query(News).filter_by(is_valid=1)

    def update_one(self, pk):
        """修改一条数据"""
        obj = self.session.query(News).get(pk)
        if obj:
            obj.is_valid = 0
            self.session.add(obj)
            self.session.commit()
            return True
        return False


    def update_more(self):
        """修改多条数据"""
        obj_list = self.session.query(News).filter_by(is_valid=1)
        for obj in obj_list:
            obj.is_valid = 0
            self.session.add(obj)
        self.session.commit()


    def delete_one(self, pk):
        """根据主键删除数据"""
        obj = self.session.query(News).get(pk)
        if obj:
            self.session.delete(obj)
            self.session.commit()  # 删除也要提交一次吖！！！这是个坑
            return True
        return False



if __name__ == '__main__':
    t = orm()
    # res = t.add_one()
    # print(res)

    # res = t.get_one()
    # print('id:{0} => {1}'.format(res.id, res.title))

    # res = t.get_more()
    # for item in res:
    #     print('id:{0} => {1}'.format(item.id, item.title))

    # res = t.update_one(1)
    # print(res)

    # res = t.update_more()
    # print(res)

    res = t.delete_one(1)
    print(res)

"""
除了查询不用commit之外，其余操作都要commit
"""