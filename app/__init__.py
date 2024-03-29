from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .settings import config

db = SQLAlchemy()


def register_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)

    from .user.view import userR, verificationR
    from .book.view import bookR, heroR
    app.register_blueprint(blueprint=userR, url_prefix='/v1/users')
    app.register_blueprint(blueprint=bookR, url_prefix='/v1/books')
    app.register_blueprint(blueprint=heroR, url_prefix='/v1/heroes')
    app.register_blueprint(blueprint=verificationR, url_prefix='/v1/verification')

    return app
