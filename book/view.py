from flask import Blueprint, request,json

bookR = Blueprint('book',__name__)

@bookR.route('/')
def hello_world():
    return 'Hello World!'

@bookR.route('/book/<book_id>',methods=['GET'])
def bookInfo(book_id):
    #return str(book_id)
    name = request.args.get('name')
    return json.jsonify(name=name,kongfu='猿王枪')

@bookR.route('/book',methods=['POST'])
def createBook():
    token = request.headers.get("token")
    print("token = ",token)
    data = json.loads(request.data)
    print(data)
    return data
