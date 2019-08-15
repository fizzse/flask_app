from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
def GenApp(name):
    app = Flask(name)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:s@106.12.147.72/fizzse?charset=utf8'
    db.init_app(app)
    return app
