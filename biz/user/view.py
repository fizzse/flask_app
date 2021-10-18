from flask import Blueprint, request, json, session
from biz.user.models import User
from biz.utils.vcode import generate_code

userR = Blueprint('user', __name__)
verificationR = Blueprint('verification', __name__)


@verificationR.route('/code')
def code():
    return generate_code()


@userR.route('/', methods=['POST'])
def create_user():
    data = json.loads(request.data)
    user = User()
    user.account = data["account"]
    user.password = data["password"]
    user.name = data["name"]
    user.create_user()
    return data


@userR.route('/login', methods=['POST'])
def login():
    data = json.loads(request.data)
    user = User.query_by_account(data['account'])

    if user is None:
        return "null"

    if user.verify_password(data['password']):
        session["account"] = user.account
        session['name'] = user.name
        return "success"

    return "null"


@userR.route('/index', methods=['GET'])
def index():
    info = {"account": session["account"], "name": session['name']}
    return info
