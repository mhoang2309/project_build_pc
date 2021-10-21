from flask import Blueprint, make_response, request, jsonify
from flask.views import MethodView

import jwt
import datetime
from functools import wraps

login_blueprint = Blueprint('uesr_blueprint',__name__)
logout_bp = Blueprint('logout',__name__)
SECRET_KEY = 'abc'


# check token
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('token')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 403
        try:
            jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        except:
            return jsonify({'message': 'Token is invalid!'}), 403
        return f(*args, **kwargs)
    return decorated


class Login(MethodView):
    def post(self):
        username = request.form['user']
        password = request.form['pass']
        print(username)
        print(password)
        if username == 'hoang' and password == '1234':
            token = jwt.encode({'user': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=720)},
                            SECRET_KEY)
            return make_response('OK', 200, {'Token': token})

        return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})
    
class Logout(MethodView):
    @token_required    
    def get(self):
        return make_response('OK Logout', 200, {'message':'Logout'})


class Register(MethodView):
    def put(self):
        return make_response('200', 200, {'user':'OK'})




login_view = Login.as_view("login_api")
login_blueprint.add_url_rule("",view_func=login_view, methods=["POST"])

logout_view = Logout.as_view("logout_api")
logout_bp.add_url_rule("", view_func=logout_view, methods=["GET"])

