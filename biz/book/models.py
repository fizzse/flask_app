from biz import db


class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    heroes = db.relationship('Hero', backref='book', lazy='dynamic')

    def create_book(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def query_by_id(book_id):
        return Book.query.filter_by(id=book_id).first()

    @staticmethod
    def list(params):
        conn = Book.query
        if params['name'] != '':
            conn = conn.filter_by(title=params['name'])
        return conn.all()


class Hero(db.Model):
    __tablename__ = 'hero'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    trick = db.Column(db.String(20), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))

    def create_hero(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def query_by_id(hero_id):
        return Hero.query.filter_by(id=hero_id).first()
