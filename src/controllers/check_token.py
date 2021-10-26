from flask import make_response, request
import jwt
from src.config.sqlalchemy import DatabaseConfig, TokenConfig
from functools import wraps
from src.models.user import Token

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine(DatabaseConfig.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
db_build_pc = Session()

def delete_token(token):
    db_build_pc.query(Token).filter_by(token=token).delete()
    db_build_pc.commit()

def is_admin(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.cookies.get('token')
        data = jwt.decode(token, options={"verify_signature": False})
        if data['is_admin'] == False:
            return make_response({'message':'not admin'}, 401)
        return f(*args, **kwargs)
    return decorated
    
# check token
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.cookies.get('token')
        
        if not token:
            return make_response({'message': 'Token is missing!'}, 403)
        try:
            jwt.decode(token, TokenConfig.SECRET_KEY, algorithms=[TokenConfig.ALGORITHMS])
            token_obj = db_build_pc.query(Token).filter_by(token=token).first()
            if token_obj:
                pass
            else:
                return make_response({'message':'Token err'}, 401)
        except:
            return make_response({'message': 'Token is invalid!'}, 403)
        return f(*args, **kwargs)

    return decorated

