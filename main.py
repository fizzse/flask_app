from flask import Flask 
from book.view import bookR
from hero.view import heroR

app = Flask(__name__)

app.register_blueprint(bookR)
app.register_blueprint(heroR)

if __name__ == '__main__':
   app.run()