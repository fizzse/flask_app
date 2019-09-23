
from .. import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    account = db.Column(db.String(20),nullable=True)
    password = db.Column(db.String(50),nullable=True)
    name  = db.Column(db.String(20))
