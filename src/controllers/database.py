from src.config.sqlalchemy import DatabaseConfig
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine(DatabaseConfig.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)

db_build_pc = Session()
