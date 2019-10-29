from flask import Blueprint, request, json
from .models import Book

bookR = Blueprint('book', __name__)


# 创建图书
@bookR.route('/', methods=['POST'])
def create_book():
    data = json.loads(request.data)
    book = Book()
    book.title = data["name"]
    book.create_book()
    return data


@bookR.route('/<book_id>', methods=['GET'])
def book_info(book_id):
    # return str(book_id)
    name = request.args.get('name')
    return json.jsonify(name=name, kongfu='猿王枪')
