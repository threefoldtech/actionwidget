

from flask import Flask
from flask import request
from validate_email import validate_email
import send_email
import email_referrer
import email_referred
import uuid
import db
import json

from db.user import User
from db.referrals_done_user import ReferralsDoneUser
from db.object_encoder import ObjectEncoder
app = Flask(__name__)


@app.route('/api/user/<email_address>',  methods=['PUT'])
def step1(email_address):
    content = request.get_json()
    
    #Check if email is valid, if user is not  in referral program already
    if not validate_email(email_address):
        return "Email address invalid", 400

    #Set fields for user
    mobile = content['mobile']
    reserve_3bot = content['reserve_3bot'] == 1 #check if we can remove this, seems obsolete
    videoconf = content['videoconf'] == 1
    social_media = content['social_media'] == 1
    farmer = content['farmer'] == 1
    deploy_it = content['deploy_it'] == 1
    gdpr = content['gdpr'] == 1
    cookies = content['cookies'] == 1
    email = content['email'] == 1
    user_referrer_token = str(uuid.uuid1())
    referral = False
    currencies = False

    #optional parameters
    if 'referral' in content:
        referral = content['referral'] == 1
    if 'currencies' in content:
        currencies = content['currencies'] == 1

    existing_user = User.get_by_email_address(email_address)
    
    #update if exists
    if existing_user is not None:
        if 'user_referrer_token' not in content:
            return "can not update a user without user_referrer_token", 400
        if existing_user.referrer_token != content['user_referrer_token']:
            return "user_referrer_token does not match", 400
        
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

        existing_user.update()
        return  existing_user.referrer_token, 200 
    
    #Insert if not
    user = User(0, email_address,user_referrer_token , mobile, reserve_3bot, videoconf, social_media, farmer, deploy_it, gdpr, cookies, email)
    user.add()

    return user_referrer_token, 200

#Update referral token, currency and send email if needed
@app.route('/api/set_referral_and_currency',  methods=['POST'])
def set_referral_and_currency():
    content = request.get_json()
    referrer_token = content['user_referrer_token']
    referral = content['referral'] == 1
    currencies = content['currencies'] == 1
    
    user = User.get_by_referrer_token(referrer_token)
    if user is None:
        return "User does not exists", 404

    user.referral = referral
    user.currencies = currencies

    user.update()

    if referral:
        # send email referral
        print("sending to ", user.email_address)
        msg = email_referrer.get_email_referrer_text(referrer_token)
        send_email.send_email(user.email_address,
                email_referrer.get_email_referrer_subject(), msg)
        print("Send complete!")
    if currencies:
        # send email currencies
        print("not implemented")

    return "true"

@app.route('/api/referral_done',  methods=['POST'])
def update_referral():
    content = request.get_json()
    #get by referrer_token
    referral_3bot_name = content['referral_3bot_name']
    user_id = content['user_id']

    user = User.get_by_id(user_id)

    if user is None:
        return "User not found", 404
    
    #if users exists, add referral => TODO check POI
    if ReferralsDoneUser.check_already_referred_email_address(referral_3bot_name):
        return "User already in referral program", 400

    referral_done = ReferralsDoneUser(0, user_id, referral_3bot_name) #if jan invites piet, user_id is jan's; email is piet's
    referral_done.add()

    return referral_3bot_name

@app.route('/api/referral_done',  methods=['GET'])
def get_referrals_done():
    content = request.get_json()
    referrer_token = content['referrer_token']

    user = User.get_by_referrer_token(referrer_token)
    if user is None:
        return "User does not exists", 404
    referrals = ReferralsDoneUser.get(user.id)

    return json.dumps(referrals,  cls=ObjectEncoder)


if __name__ == '__main__':
    db.init()
    app.run(debug=True)
