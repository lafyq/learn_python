# 导入:
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类
Base = declarative_base()

# 定义User对象：
class User(Base):
    # 表的名字
    __tablename__ = 'userTest'

    # 表的结构
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# 初始化数据库连接：
engine = create_engine('mysql+mysqlconnector://root: @localhost:3306/test')

# 创建DBSession类型
DBSession = sessionmaker(bind=engine)


"""  下面，我们看看如何向数据库表中添加一行记录。  """
# 创建session对象
session = DBSession()
# 创建新User对象
new_user = User(id='5', name='bob')
# 添加到session中
session.add(new_user)
# 提交保存到数据库
session.commit()
# 关闭session
session.close()

"""
可见，关键是获取session，然后把对象添加到session，最后提交并关闭。DBSession对象可视为当前数据库连接。

如何从数据库表中查询数据呢？有了ORM，查询出来的可以不再是tuple，而是User对象。SQLAlchemy提供的查询接口如下：
"""
# 创建session
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行：
user = session.query(User).filter(User.id=='5').one()
# 打印类型和对象的name属性
print('type: ', type(user))
print('name: ', user.name)
# 关闭session
session.close()