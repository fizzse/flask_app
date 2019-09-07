from flask_sqlalchemy import SQLAlchemy
from .. import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    account = db.Column(db.String(20),nullable=True)
    password = db.Column(db.String(50),nullable=True)
    name  = db.Column(db.String(20))

class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)

