from src.controllers.health_check import health_check_bp
from src.controllers.user import login_blueprint, logout_bp

def register_blueprint(app):
    app.register_blueprint(health_check_bp, url_prefix="/health_check")
    app.register_blueprint(login_blueprint, url_prefix="/login")
    app.register_blueprint(logout_bp, url_prefix="/logout")