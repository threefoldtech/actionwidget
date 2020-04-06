

from flask import Flask
from flask import request
from validate_email import validate_email

import uuid
import db
import json
import responses
from urllib.request import urlopen
import config
import nacl

from db.user import User

from db.object_encoder import ObjectEncoder
app = Flask(__name__)


@app.route('/api/user',  methods=['PUT'])
def put_user():
    content = request.get_json()

    email_address = content['email_address']
    # check if email is valid, if user is not  in referral program already
    if not validate_email(email_address):
        return responses.errorObj(400, "email_address invalid")
    name = content['name']

    user = User(0, email_address,name)
    user.add()

    return responses.successObj(200, user)

@app.route('/api/user',  methods=['GET'])
def get_users():
    if request.headers['x-api-key'] != config.api_key:
        return responses.errorObj(401, "Unauthorized")

    all_users = User.get()

    return responses.successObj(200, all_users)



if __name__ == '__main__':
    db.init()
    app.run(debug=True)
