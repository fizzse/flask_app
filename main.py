from flask import Flask

from app.book.view import bookR
from app.user.view import userR
from app import GenApp

app = GenApp(__name__)
app.register_blueprint(blueprint=bookR, url_prefix='/v1/books')
app.register_blueprint(blueprint=userR, url_prefix='/v1/users')

@app.route('/v1/ping')
def pong():
    return 'pong!'

if __name__ == '__main__':
    app.run()
