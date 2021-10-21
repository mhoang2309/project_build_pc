from flask import Flask, jsonify, request, make_response
import jwt
import datetime
from functools import wraps
from src.controllers.user import login, logout, register

from src.blueprint_register import register_blueprint

app = Flask(__name__)
register_blueprint(app)
# app.config['SECRET_KEY'] = 'abc'
# def token_required(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         token = request.headers.get('token')
#         if not token:
#             return jsonify({'message': 'Token is missing!'}), 403
#         try:
#             jwt.decode(token, app.config['SECRET_KEY'])
#         except:
#             return jsonify({'message': 'Token is invalid!'}), 403
#         return f(*args, **kwargs)
#     return decorated

# @app.route('/health_check', methods = ['GET'])
# def health_check():
#     return make_response('OK', 200, { 'message': "Server is and running" })


# @app.route('/login', methods = ['POST'])
# def Login():
#     username = request.form['user']
#     password = request.form['pass']
#     if username == 'hoang' and password == '123':
#         token = jwt.encode({'user': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=100)},
#                            app.config['SECRET_KEY'])
#         return make_response('OK', 200, {'Token': token})

#     return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})

#     # return login(username, password)
# @app.route('/logout', methods = ['GET'])
# @token_required
# def Logout():
#     return logout()


# @app.route('/login', methods=['GET'])
# def hello_world():
#     if 'username' in request.args:
#         username = request.args['username']
#     else:
#         username = '0'
#     if 'password' in request.args:
#         password = request.args['password']
#     else:
#         password = '0'
#     return Index(username, password)
#
# @app.route('/test', methods=['POST'])
# def test():
#     username = request.json['user']
#     password = request.json['pass']
#     return Index(username, password)
#
# @app.route('/app', methods=['POST'])
# def post_app():
#     name = request.json['name']
#     return name


if __name__ == '__main__':
    app.run()
