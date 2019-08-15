from flask import Flask 
from book.view import bookR
from hero.view import heroR

app = Flask(__name__)

app.register_blueprint(blueprint=bookR, url_prefix='/v1')
app.register_blueprint(blueprint=heroR, url_prefix='/v1')

@app.route('/v1/ping')
def pong():
    return 'pong!'

if __name__ == '__main__':
   app.run()