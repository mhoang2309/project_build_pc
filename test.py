import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy import engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    """User model"""
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement = True)
    username = Column(String(25), unique=True, nullable=False)
    password = Column(String(), unique=False, nullable=False)
    is_admin = Column(Boolean, unique=False, nullable=False, default=0)


if __name__ == "__main__":
        engine = create_engine('postgresql://postgres:admin@localhost:5432/porject_build_pc')
        Base.metadata.create_all(engine)