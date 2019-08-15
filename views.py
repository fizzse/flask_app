from flask import Flask ,json,request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/book/<book_id>',methods=['GET'])
def bookInfo(book_id):
    #return str(book_id)
    name = request.args.get('name')
    return json.jsonify(name=name,kongfu='猿王枪')

@app.route('/book',methods=['POST'])
def createBook():
    token = request.headers.get("token")
    print("token = ",'hello')
    return token
    # data = json.loads(request.data)
    # print(data)
    # return data + token

@app.route('/heros')
def hero():
    # token = request.headers.get("token")
    # print("token = ",'hello')
    return "hello hello hello"