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

def is_admin(token):
    data = jwt.decode(token, options={"verify_signature": False})
    print(data)
    

# check token
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('token')
        
        if not token:
            return make_response({'message': 'Token is missing!'}, 403)
        try:
            jwt.decode(token, TokenConfig.SECRET_KEY, algorithms=[TokenConfig.ALGORITHMS])
            is_admin(token)
            token_obj = db_build_pc.query(Token).filter_by(token=token).first()
            if token_obj:
                delete_token(token)
            else:
                return make_response({'message':'Token err'}, 401)
        except:
            return make_response({'message': 'Token is invalid!'}, 403)
        return f(*args, **kwargs)

        # data  = data = decoded = jwt.decode(token, options={"verify_signature": False}) 
        # username = data['user']
        # for i in db_build_pc.query(User).\
        #         filter(User.username==username): 
        #     if not token:
        #         return jsonify({'message': 'Token is missing!'}), 403
        #     try:
        #         jwt.decode(token, i.key, algorithms=["HS256"])
        #     except:
        #         return jsonify({'message': 'Token is invalid!'}), 403
        #     return f(*args, **kwargs)
    return decorated

