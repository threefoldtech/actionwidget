import json
from db.object_encoder import ObjectEncoder

def successObj(code, data):
    return json.dumps({ 'succes': True, 'data': data }, cls=ObjectEncoder), code

def errorObj(code, message):
    return json.dumps({ 'error': { 'code': code, 'message': message} },  cls=ObjectEncoder), code