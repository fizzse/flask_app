import jwt

def generate_token(payload:dict, screct_key: str, algorithms: str):
    token = ''
    try:
        token = jwt.encode(payload, key=screct_key, algorithm=algorithms)
    except :
        raise
    return token

def verify_token(screct_key: str,token:str, algorithms: str):
    data = {}

    try:
        data = jwt.decode(token, key=screct_key, algorithms=algorithms)
    except :
        raise

    return data