from biz import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=True)
    password = db.Column(db.String(50), nullable=True)
    created_at = db.Column(db.DateTime,nullable=False,default=datetime.now)
    auths = db.relationship('UserAuth',back_populates = 'user')

    def create_user(self):
        db.session.add(self)
        db.session.commit()

    def verify_password(self, password):
        return self.password == password

    @staticmethod
    def query_by_account(account):
        return User.query.filter_by(name=account).first()


class UserAuth(db.Model):
    __tablename__ = 'user_auth'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    name = db.Column(db.String(20), nullable=True)
    value = db.Column(db.String(20), nullable=True)
    created_at = db.Column(db.DateTime,nullable=False,default=datetime.now)
    user = db.relationship('User',back_populates = 'auths')

    @staticmethod
    def query_by_auth(name,value):
        return UserAuth.query.filter_by(name=name,value=value).first()