import sqlalchemy as orm
import pymysql as sql
from sqlalchemy import create_engine, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy import Column, String, Integer, Text
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime
import mysql_rock_pwd

#'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = mysql_rock_pwd.get_engine("tu_share")
Base = declarative_base()

# 定义User对象:
class Stock(Base):
    # 表的名字:
    __tablename__ = 'stock_price'

    # 表的结构:
    code = orm.Column(orm.String(20), primary_key=True)
    name = orm.Column(orm.String(100))
    price =orm.Column(orm.Float)
    open = orm.Column(orm.Float)
    pre_close = orm.Column(orm.Float)
    high = orm.Column(orm.Float)
    low = orm.Column(orm.Float)
    price_date = orm.Column(orm.DateTime)


DBSession = orm.orm.sessionmaker(bind=engine)

#------------Query------------
# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(Stock).filter(Stock.code=='111').first()
# 打印类型和对象的name属性:
print ('type:', type(user))
#print ('name:', user.name)
# 关闭Session:
user.name="Rock"
session.add(user)
session.delete(user)
session.rollback();
session.close()

lists= session.query(Stock).all()
for u in lists:
    print (u.code, u.name, u.price);


#-------------Insert----------------

# 创建session对象:
session = DBSession()
# 创建新User对象:
new_stock = Stock(code='222', name='Bob', price=9.99, price_date= datetime.now(), high=0.0, low=0.0, pre_close=0.0, open=0.0)
# 添加到session:
session.add(new_stock)
# 提交即保存到数据库:
session.commit()
session.delete(user)
session.commit()
# 关闭session:
session.close()



