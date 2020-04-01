

from flask import Flask
from flask import request
from validate_email import validate_email
import send_email
import email_referrer
import email_referred
import uuid
import db
import json
import responses

from db.user import User
from db.referrals_done_user import ReferralsDoneUser
from db.object_encoder import ObjectEncoder
app = Flask(__name__)


@app.route('/api/user',  methods=['PUT'])
def step1():
    content = request.get_json()

    email_address = content['email_address']
    # check if email is valid, if user is not  in referral program already
    if not validate_email(email_address):
        return responses.errorObj(400, "email_address invalid")

    # set fields for user
    mobile = content['mobile']
    reserve_3bot = content['reserve_3bot'] == 1 # check if we can remove this, seems obsolete
    videoconf = content['videoconf'] == 1
    social_media = content['social_media'] == 1
    farmer = content['farmer'] == 1
    deploy_it = content['deploy_it'] == 1
    gdpr = content['gdpr'] == 1
    cookies = content['cookies'] == 1
    email = content['email'] == 1
    referral_url = content['referral_url']

    # optional parameters
    if 'referral' in content:
        referral = content['referral'] == 1
    if 'currencies' in content:
        currencies = content['currencies'] == 1

    existing_user = None
    if 'user_referrer_token' in content:
        existing_user = User.get_by_referrer_token(content['user_referrer_token'])

    # update if exists
    if existing_user is not None:
        existing_user.mobile = mobile
        existing_user.reserve_3bot = reserve_3bot
        existing_user.videoconf = videoconf
        existing_user.social_media = social_media
        existing_user.farmer = farmer
        existing_user.deploy_it = deploy_it
        existing_user.gdpr = gdpr
        existing_user.cookies = cookies
        existing_user.email = email
        existing_user.referral = referral
        existing_user.currencies = currencies
        existing_user.referral_url = referral_url
        existing_user.update()
        return  responses.successObj(200, {"user_referrer_token": existing_user.referrer_token })
    
    # Insert if not
    user_referrer_token = str(uuid.uuid4())
    user_verify_token = str(uuid.uuid4())

    user = User(0, email_address,user_referrer_token, user_verify_token, referral_url, mobile, reserve_3bot, videoconf, social_media, farmer, deploy_it, gdpr, cookies, email)
    user.add()
    print("here")
    return responses.successObj(200, {"user_referrer_token": user.referrer_token })



@app.route('/api/verify_user/<user_verify_token>',  methods=['POST'])
def verify(user_verify_token):
   
    user = User.get_by_verify_token(user_verify_token)
    if user is None:
         return responses.errorObj(404, "User not found")
    user.verified = True
    user.update()

    return responses.successObj(200, user)


#Update referral token, currency and send email if needed
@app.route('/api/set_referral_and_currency',  methods=['POST'])
def set_referral_and_currency():
    content = request.get_json()
    referrer_token = content['user_referrer_token']
    referral = content['referral'] == 1
    currencies = content['currencies'] == 1
    
    user = User.get_by_referrer_token(referrer_token)
    if user is None:
        return responses.errorObj(404, "User does not exists")

    user.referral = referral
    user.currencies = currencies

    user.update()

    if referral:
        # send email referral
        print("sending to ", user.email_address)
        msg = email_referrer.get_email_referrer_text(user.verify_token)
        send_email.send_email(user.email_address,
                email_referrer.get_email_referrer_subject(), msg)
        print("Send complete!")
    if currencies:
        # send email currencies
        print("not implemented")

    return responses.successObj(200, { "referral" : referral, "currencies": currencies})

@app.route('/api/referral_done',  methods=['POST']) #TODO POI!!!
def update_referral():
    content = request.get_json()
    #get by referrer_token
    referral_3bot_name = content['referral_3bot_name']
    user_id = content['user_id']

    user = User.get_by_id(user_id)

    if user is None:
        return responses.errorObj(404, "User not found")
    
    #if users exists, add referral => TODO check POI
    if ReferralsDoneUser.check_already_referred_3bot_name(referral_3bot_name):
        return responses.successObj(200,referral_3bot_name) # the user installed 3bot connect so this is ok

    referral_done = ReferralsDoneUser(0, user_id, referral_3bot_name) #if jan invites piet, user_id is jan's; email is piet's
    referral_done.add()

    return responses.successObj(200,referral_3bot_name)

@app.route('/api/referral_done/<user_referrer_token>',  methods=['GET'])
def get_referrals_done(user_referrer_token):

    user = User.get_by_referrer_token(user_referrer_token)
    if user is None:
         return responses.errorObj(404, "User not found")
    referrals = ReferralsDoneUser.get(user.id)

    return responses.successObj(200,json.dumps(referrals,  cls=ObjectEncoder))


if __name__ == '__main__':
    db.init()
    app.run(debug=True)
