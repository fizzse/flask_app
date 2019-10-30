from flask import Blueprint, request, json
from .models import Book, Hero

bookR = Blueprint('book', __name__)
heroR = Blueprint('hero', __name__)


# 创建图书
@bookR.route('/', methods=['POST'])
def create_book():
    data = json.loads(request.data)
    book = Book()
    book.title = data["name"]
    book.create_book()
    return data


# 图书列表
@bookR.route('/', methods=['GET'])
def book_list():
    params = {}
    name = request.args.get('name', "")
    params['name'] = name
    books = Book.list(params)
    res = []
    for book in books:
        res.append({'id': book.id, 'title': book.title})
    return json.jsonify(res)


@bookR.route('/<book_id>', methods=['GET'])
def book_info(book_id):
    book = Book.query_by_id(book_id)

    heroes = []
    for v in book.heroes:
        heroes.append({'name': v.name, 'trick': v.trick})
    res = {"title": book.title, "heroes": heroes}
    return json.jsonify(res)


@heroR.route('/<hero_id>', methods=['GET'])
def hero_info(hero_id):
    hero = Hero.query_by_id(hero_id)

    h = {'name': hero.name, 'trick': hero.trick}
    res = {"title": hero.book.title, "hero": h}
    return json.jsonify(res)
