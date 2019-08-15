from flask import Flask

from app.book.view import bookR
from app.hero.view import heroR
from app import GenApp

app = GenApp(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:s@106.12.147.72/fizzse?charset=utf8'

app.register_blueprint(blueprint=bookR, url_prefix='/v1')
app.register_blueprint(blueprint=heroR, url_prefix='/v1')

@app.route('/v1/ping')
def pong():
    return 'pong!'

if __name__ == '__main__':
    app.run()
