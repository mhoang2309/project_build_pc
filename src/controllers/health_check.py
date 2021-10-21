from flask import Blueprint, make_response
from flask.views import MethodView

health_check_bp = Blueprint('health_check_bp', __name__)

class HealthCheck(MethodView):
    def get(self):
        return make_response('OK', 200, { 'message': "Server is and running" })
    # def post(self):
    #     pass
    # def put(self):
    #     pass
    # def delete(self):
    #     pass

health_check_view = HealthCheck.as_view("health_check_api")

health_check_bp.add_url_rule(
    "", view_func=health_check_view, methods=["GET"]
)


# # User
# # GET /users
# # GET /users/:user_id
# class Users(MethodView):
#     def get(self, user_id):
#         return make_response('OK', 200, { 'message': "Server is and running" })
    
# class User(MethodView):

