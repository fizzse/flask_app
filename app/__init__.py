from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .settings import config

db = SQLAlchemy()


def register_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)

    from .user.view import userR
    from .book.view import bookR
    app.register_blueprint(blueprint=userR, url_prefix='/v1/users')
    app.register_blueprint(blueprint=bookR, url_prefix='/v1/books')
    return app
