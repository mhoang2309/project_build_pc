from flask import Flask, jsonify, request, make_response

from src.blueprint_register import register_blueprint

app = Flask(__name__)
register_blueprint(app)

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
