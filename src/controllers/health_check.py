from flask import Blueprint, make_response, request
from flask.views import MethodView


from src.models.user import User
from flask_sqlalchemy import SQLAlchemy

db_build_pc = SQLAlchemy()

health_check_bp = Blueprint('health_check_bp', __name__)

class HealthCheck(MethodView):
    def put(self):
        username = request.form['user']
        password = request.form['pass']
        print(username)
        # check username exists
        user_obj = User.query.filter_by(username=username).first()
        if user_obj:
            return "1"
        user = User(username=username, password=password)
        db_build_pc.session.add(user)
        db_build_pc.session.commit()
        return make_response('OK', 200, { 'message': "Server is and running" })
    # def post(self):
    #     pass
    # def put(self):
    #     pass
    # def delete(self):
    #     pass

health_check_view = HealthCheck.as_view("health_check_api")

health_check_bp.add_url_rule("", view_func=health_check_view, methods=["PUT"])


# # User
# # GET /users
# # GET /users/:user_id
# class Users(MethodView):
#     def get(self, user_id):
#         return make_response('OK', 200, { 'message': "Server is and running" })
    
# class User(MethodView):

