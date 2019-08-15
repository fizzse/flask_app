from flask import Flask

from book.view import bookR
from hero.view import heroR
from service import server

app = server.GenApp(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:s@106.12.147.72/fizzse?charset=utf8'

app.register_blueprint(blueprint=bookR, url_prefix='/v1')
app.register_blueprint(blueprint=heroR, url_prefix='/v1')

@app.route('/v1/ping')
def pong():
    return 'pong!'


#server.db.create_all()

if __name__ == '__main__':
    app.run()
