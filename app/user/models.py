from .. import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    account = db.Column(db.String(20), nullable=True)
    password = db.Column(db.String(50), nullable=True)
    name = db.Column(db.String(20))

    def create_user(self):
        db.session.add(self)
        db.session.commit()

    def verify_password(self, password):
        return self.password == password

    @staticmethod
    def query_by_account(account):
        return User.query.filter_by(account=account).first()


