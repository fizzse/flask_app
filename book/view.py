from flask import Blueprint, request,json
#from ..service import model
bookR = Blueprint('book',__name__)

# 创建图书
@bookR.route('/books',methods=['POST'])
def createBook():
    data = json.loads(request.data)
    # book = model.Book()
    # book.title = "笑傲江湖"
    # book.
    return data

@bookR.route('/book/<book_id>',methods=['GET'])
def bookInfo(book_id):
    #return str(book_id)
    name = request.args.get('name')
    return json.jsonify(name=name,kongfu='猿王枪')



