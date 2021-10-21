from enum import unique

from sqlalchemy.orm import defer
from app import db_build_pc
from sqlalchemy import Column, Integer, String, Boolean

class User(db_build_pc.Model):
    """User model"""
    __tablename__ = 'user'
    id = db_build_pc.Column(db_build_pc.Integer, primary_key=True, autoincrement = True)
    username = db_build_pc.Column(db_build_pc.String(25), unique=True, nullable=False)
    passwrod = db_build_pc.Column(db_build_pc.String(), unique=False, nullable=False)
    key = db_build_pc.Column(db_build_pc.String(), unique=False, nullable=True)
    is_admin = db_build_pc.Column(db_build_pc.Boolean, unique=False, nullable=False, default=0)
    db_build_pc.create_all()