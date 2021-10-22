from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from flask_sqlalchemy import SQLAlchemy

db_build_pc = SQLAlchemy()

class User(db_build_pc.Model):
    """User model"""
    __tablename__ = 'user'
    id = db_build_pc.Column(db_build_pc.Integer, primary_key=True, autoincrement = True)
    username = db_build_pc.Column(db_build_pc.String(25), unique=True, nullable=False)
    password = db_build_pc.Column(db_build_pc.String(), unique=False, nullable=False)
    is_admin = db_build_pc.Column(db_build_pc.Boolean, unique=False, nullable=False, default=0)

class Token(db_build_pc.Model):
    """Token user"""
    id = db_build_pc.Column(Integer, primary_key=True, autoincrement = True)
    username = db_build_pc.Column(String(25), ForeignKey(User.username), unique=False, nullable=False)
    token = db_build_pc.Column(String(), unique=False, nullable=False)


if __name__ == "__main__":
        db_build_pc.create_all()