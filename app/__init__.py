from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .settings import config

db = SQLAlchemy()
def GenApp(configName):
    app = Flask(__name__)
    app.config.from_object(config[configName])
    db.init_app(app)
    return app