from flask_sqlalchemy import SQLAlchemy
from server import db

class Stu(db.Model):
    __tablename__ = 'stu'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

