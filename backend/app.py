

from flask import Flask
from flask import request
from validate_email import validate_email

import uuid
import db
import json
import responses
from urllib.request import urlopen
from mount import config
import nacl

from db.user import User

from db.object_encoder import ObjectEncoder
app = Flask(__name__)


@app.route('/api/user',  methods=['PUT'])
def put_user():
    content = request.get_json()

    email_address = content['email_address']
    internet_capacity = content['internet_capacity'] == 1
    deploy_solutions = content['deploy_solutions'] == 1
    # check if email is valid, if user is not  in referral program already
    if not validate_email(email_address):
        return responses.errorObj(400, "email_address invalid")
    name = content['name']
    
    double_name = None
    if 'double_name' in content:
        double_name = content['double_name']
        print("checkign taken", double_name)
        if User.check_double_name_taken(double_name):
            return responses.errorObj(409, "double_name is taken")

    user = User(0, email_address, name, double_name, internet_capacity, deploy_solutions)
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
