from flask import Blueprint, request,json,session
from .models import User
from .. import db
userR = Blueprint('user',__name__)

@userR.route('/ping')
def Pong():
    return 'pong pong...'


@userR.route('/',methods=['POST'])
def createUser():
    data = json.loads(request.data)
    user = User()
    user.account = data["account"]
    user.password = data["password"]
    user.name = data["name"]
    db.session.add(user)
    db.session.commit()
    return data

@userR.route('/login',methods=['POST'])
def login():
    data = json.loads(request.data)
    user = User.query.filter_by(account=data["account"]).first()
    if user.password == data["password"]:
       session["account"] = user.account
       session['name'] = user.name
       return "success"
    
    return "haha"

@userR.route('/index',methods=['GET'])
def index():
    info = {}
    info["account"] = session["account"]
    info["name"] = session['name'] 
    return info