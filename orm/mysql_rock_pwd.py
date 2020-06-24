import sqlalchemy as orm

def get_engine(dbname):
    engine = orm.create_engine("mysql+pymysql://rock:mysql.******@120.79.213.203:3306/" + dbname+"?charset=utf8", max_overflow=5,encoding='utf-8')
    return engine