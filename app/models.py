from sqlalchemy import (Column,
                        ForeignKey,
                        Integer,
                        String,
                        Boolean,
                        DateTime,
                        Date
                        )

from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import generate_password_hash, check_password_hash

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True, nullable=False)
    email = Column(String(48), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
    telegram_id = Column(Integer())
    first_name = Column(String(32), nullable=True)
    last_name = Column(String(32), nullable=True)
    is_superuser = Column(Boolean)
    archive = Column(Boolean)
    mailing = Column(Boolean)
    last_logon = Column(DateTime)
    task = relationship('Task', backref='user')

    def __repr__(self):
        return f'<User {self.username}>'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Task(Base):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True)
    task_api_id = Column(Integer)
    title = Column(String)
    name_organization = Column(String)
    deadline = Column(Date)
    category_id = Column(Integer, ForeignKey('category.id'))
    bonus = Column(Integer)
    location = Column(String)
    link = Column(String)
    description = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))

    def __repr__(self):
        return f'<Task {self.title}>'


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    category_api_id = Column(Integer)
    name = Column(String(100))
    task = relationship('Task', backref='category')

    def __repr__(self):
        return f'<Category {self.name}>'
