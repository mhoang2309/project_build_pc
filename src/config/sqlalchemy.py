import os
from dotenv import load_dotenv

load_dotenv()
class Config(object):
    DEBUG = eval(os.getenv('DEBUG_FLASK', default=False))
    FLASK_RUN_PORT = os.getenv('FLASK_RUN_PORT', default=3000)
    
class DatabaseConfig(Config):

    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = eval(os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS'))

class TokenConfig(Config):
    SECRET_KEY = os.getenv('SECRET_KEY')
    ALGORITHMS = os.getenv('ALGORITHMS')

class HashPasswordConfig(Config):
    METHOD = os.getenv('METHOD')
    SALT_LENGTH = os.getenv('SALT_LENGTH')