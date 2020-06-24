# coding: utf-8
import random
from faker import Factory

from sqlalchemy import create_engine, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy import Column, String, Integer, Text
from sqlalchemy.orm import sessionmaker, relationship

import mysql_rock_pwd

Base = declarative_base()
engine = mysql_rock_pwd.get_engine("test")

class UserInfo(Base):
    __tablename__ = 'blog_userinfos'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    qq = Column(String(11))
    phone = Column(String(20))
    link = Column(String(64))
    user_id = Column(Integer, ForeignKey('blog_users.id'))


class Article(Base):
    __tablename__ = 'blog_articles'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False, index=True)
    content = Column(Text)
    user_id = Column(Integer, ForeignKey('blog_users.id'))
    cate_id = Column(Integer, ForeignKey('blog_categories.id'))
    tags = relationship('Tag', secondary='blog_article_tag', backref='blog_articles')

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.title)

class User(Base):

    __tablename__ = 'blog_users'

    id = Column(Integer, primary_key=True)
    username = Column(String(64), nullable=False, index=True)
    password = Column(String(64), nullable=False)
    email = Column(String(64), nullable=False, index=True)
    articles = relationship('Article', backref='author')
    userinfo = relationship('UserInfo', backref='blog_user', uselist=False)

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.username)


class Category(Base):

    __tablename__ = 'blog_categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False, index=True)
    articles = relationship('Article', backref='category')

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.name)


article_tag = Table(
    'blog_article_tag', Base.metadata,
    Column('article_id', Integer, ForeignKey('blog_articles.id')),
    Column('tag_id', Integer, ForeignKey('blog_tags.id'))
)


class Tag(Base):
    __tablename__ = 'blog_tags'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False, index=True)
    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.name)


if __name__ == '__main__':
    print("Create blog schema...")
    Base.metadata.create_all(engine)

    faker = Factory.create()
    Session = sessionmaker(bind=engine)
    session = Session()

    faker_users=[]
    for i in range(10):
        userinfo = UserInfo(name=faker.name(), qq=faker.random_element(), link=faker.sentence(),
                                   phone=faker.phone_number())
        user = User(username=faker.name(), password=faker.word(), email=faker.email())
        user.userinfo = userinfo
        print("Add users...")
        #session.add(user)
        #session.commit();
        #print("users id.." + str(user.id))
        faker_users.append(user)

    session.add_all(faker_users)

    print("Add category...")
    faker_categories = [Category(name=faker.word()) for i in range(10)]
    session.add_all(faker_categories)

    print("Add tags...")
    faker_tags= [Tag(name=faker.word()) for i in range(20)]
    session.add_all(faker_tags)
    print("Add article...")

    for i in range(100):
        article = Article(
            title=faker.sentence(),
            content=' '.join(faker.sentences(nb=random.randint(10, 20))),
            author=random.choice(faker_users),
            category=random.choice(faker_categories)
        )
        for tag in random.sample(faker_tags, random.randint(2, 5)):
            article.tags.append(tag)

        session.add(article)

    session.commit()