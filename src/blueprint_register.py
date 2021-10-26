from src.controllers.user import login_blueprint, logout_bp, register_bp
from src.controllers.part import  parts_bp
def register_blueprint(app):
    # user
    app.register_blueprint(login_blueprint, url_prefix="/login")
    app.register_blueprint(logout_bp, url_prefix="/logout")
    app.register_blueprint(register_bp, url_prefix="/register")
    # 
    app.register_blueprint(parts_bp, url_prefix="/parts_api")

