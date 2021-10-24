from flask import Blueprint, make_response, request
from flask.views import MethodView

import jwt
import datetime

from src.controllers.check_token import token_required

# import random
# import string
# from passlib.hash import sha256_crypt
from werkzeug.security import generate_password_hash, check_password_hash

from src.models.user import User, Token
# from flask_sqlalchemy import SQLAlchemy

# db_build_pc = SQLAlchemy()

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine



engine = create_engine('postgresql://postgres:admin@localhost:5432/porject_build_pc')
Session = sessionmaker(bind=engine)
db_build_pc = Session()


# Bulueprint
login_blueprint = Blueprint('uesr_blueprint',__name__)
logout_bp = Blueprint('logout',__name__)
register_bp = Blueprint('register', __name__)

SECRET_KEY = 'XsPXqMwdor'



# def ramdum_key():
#     # printing letters
#     letters = string.ascii_letters
#     return ''.join(random.choice(letters) for i in range(10))

def clear_token():
    pass

class Login(MethodView):
    def post(self):
        username = request.json['user']
        password = request.json['pass']

        user_obj = db_build_pc.query(User).filter_by(username=username).first()
        if user_obj:
            for i in db_build_pc.query(User).\
                filter(User.username==username):
                if check_password_hash(i.password, password):
                    # new token "algorithms:HS256"
                    token = jwt.encode({'user': username, 'is_admin': i.is_admin, 'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=720)},
                    SECRET_KEY)
                    # token = jwt.encode({'user': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=720)},
                    #                 i.key)
                    set_token = Token(username=username, token=token)
                    db_build_pc.add(set_token)
                    db_build_pc.commit()
                    resp = make_response({'message':'OK'}, 200)
                    resp.set_cookie("token",token)
                    return resp
                return make_response({'message':'user and password'}, 401)

        return make_response({'message':'Could not verify!'}, 401)
    
class Logout(MethodView):
    @token_required    
    def get(self):  
        resp = make_response({'message':'OK Logout'}, 200, {'message':'Logout'})
        resp.delete_cookie('token')
        return resp
   
    


class Register(MethodView):
    def put(self):
        username = request.json['user']
        password = generate_password_hash(request.json['pass'], method='pbkdf2:sha256', salt_length=16)
        # check username exists
        user_obj = db_build_pc.query(User).filter_by(username=username).first()
        if user_obj:
            return make_response({'message':'Username exists'}, 401, {'user':'False'})
        add_user = User(username=username, password=password)
        db_build_pc.add(add_user)
        db_build_pc.commit()
        return make_response({'message':'Added user successfully'}, 200, {'user':'OK'})



# methods Login API
login_view = Login.as_view("login_api")
login_blueprint.add_url_rule("",view_func=login_view, methods=["POST"])
#  methods Logout API
logout_view = Logout.as_view("logout_api")
logout_bp.add_url_rule("", view_func=logout_view, methods=["GET"])
# methods register API
register_view = Register.as_view("register_api")
register_bp.add_url_rule("", view_func=register_view, methods=["PUT"])

