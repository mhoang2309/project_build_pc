from src.config.sqlalchemy import DatabaseConfig
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy import engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine(DatabaseConfig.SQLALCHEMY_DATABASE_URI)
Base.metadata.create_all(engine)
class Part(Base):
    """UsParter model"""
    __tablename__ = 'part'
    id = Column(Integer, primary_key=True, autoincrement = True)
    name = Column(String(), unique=True, nullable=False)
    type = Column(String(), unique=False, nullable=False)
    price = Column(Numeric(10, 2), unique=False, nullable=True, default=0)
