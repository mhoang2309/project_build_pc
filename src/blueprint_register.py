from src.controllers.health_check import health_check_bp

def register_blueprint(app):
    app.register_blueprint(health_check_bp, url_prefix="/health_check")