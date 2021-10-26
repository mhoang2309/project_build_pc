from logging import debug
from flask import Flask
from src.config.sqlalchemy import DatabaseConfig
from src.blueprint_register import register_blueprint

app = Flask(__name__)
app.config.from_object(DatabaseConfig())


register_blueprint(app)


if __name__ == '__main__':
    print(app.config['DEBUG'])
    app.run(port=app.config['FLASK_RUN_PORT'])