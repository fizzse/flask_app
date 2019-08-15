from flask import Blueprint, request

heroR = Blueprint('hero',__name__)

@heroR.route('/ping')
def Pong():
    return 'pong pong...'