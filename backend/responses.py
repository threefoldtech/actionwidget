import json


def successObj(code, data):
    return json.dumps({ 'succes': True, 'data': data }), code

def errorObj(code, message):
    return json.dumps({ 'error': { 'code': code, 'message': message} }), code