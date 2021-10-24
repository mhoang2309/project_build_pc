from flask import make_response, request
import jwt
from functools import wraps
from src.models.user import Token

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:admin@localhost:5432/porject_build_pc')
Session = sessionmaker(bind=engine)
db_build_pc = Session()

SECRET_KEY = 'XsPXqMwdor'

# check token
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('token')
        
        if not token:
            return make_response({'message': 'Token is missing!'}, 403)
        try:
            jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            token_obj = db_build_pc.query(Token).filter_by(token=token).first()
            if token_obj:
                db_build_pc.query(Token).filter_by(token=token).delete()
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