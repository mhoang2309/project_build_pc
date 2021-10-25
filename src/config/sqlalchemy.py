class Config(object):
    DEBUG = True
    FLASK_RUN_PORT = 5000
    
class DatabaseConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin@localhost:5432/porject_build_pc'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class TokenConfig(Config):
    SECRET_KEY = 'XsPXqMwdor'
    ALGORITHMS = 'HS256'

class HashPasswordConfig(Config):
    METHOD = 'pbkdf2:sha256'
    SALT_LENGTH = 16