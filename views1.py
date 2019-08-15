from views import app

@app.route('/ping')
def Pong():
    return 'pong pong..'