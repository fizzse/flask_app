from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from svc.config import config

db = SQLAlchemy()


def register_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)

    from biz.user.view import userR, verificationR
    from biz.book.view import bookR, heroR
    app.register_blueprint(blueprint=userR, url_prefix='/v1/users')
    app.register_blueprint(blueprint=bookR, url_prefix='/v1/books')
    app.register_blueprint(blueprint=heroR, url_prefix='/v1/heroes')
    app.register_blueprint(blueprint=verificationR, url_prefix='/v1/verification')

    @app.route("/")
    def hello_world():
        return "<p>Hello, World!</p>"

    return app

def migrate_db(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)

    db.create_all()