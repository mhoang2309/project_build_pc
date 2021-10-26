from src.config.sqlalchemy import DatabaseConfig
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy import engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine(DatabaseConfig.SQLALCHEMY_DATABASE_URI)
Base.metadata.create_all(engine)
class User(Base):
    """User model"""
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement = True)
    username = Column(String(25), unique=True, nullable=False)
    password = Column(String(), unique=False, nullable=False)
    is_admin = Column(Boolean, unique=False, nullable=False, default=0)

class Token(Base):
    """Token user"""
    __tablename__ = 'token'
    token = Column(String(), primary_key=True,)
    username = Column(String(25),ForeignKey(User.username), unique=False, nullable=False, )

