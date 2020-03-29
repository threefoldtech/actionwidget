
import sqlite3
from flask import Flask
from flask import request
from validate_email import validate_email
import send_email
import email_referrer
import email_referred
import uuid
app = Flask(__name__)


def db():

    db_api = sqlite3.connect('calltoaction.db')
    return db_api


@app.route('/')
def index():
    return "yo hello"


# {
# "email" : "{email}", //regex check
# "mobile" : "mobile",
# "reserve_3bot" : true,
# "videoconf" : true,
# "social_media": true,
# "farmer" : true,
# "deploy_it" : true,
# "gdpr: true,
# "cookies": true,
# "email" : true
# }


@app.route('/api/step1',  methods=['POST'])
def step1():
    content = request.get_json()
    con = db()
    with con:
        cursor =  con.cursor()
        email_address = content['email_address']

        #Check if email is valid, if user is not  in referral program already
        if not validate_email(email_address):
            return "Email address invalid", 400
        cursor.execute("SELECT id FROM users where email=?", [email_address])
        user_exists = cursor.fetchone()
        if user_exists is not None:
            return "User is already registered", 409 
       
        #Register user
        mobile = content['mobile']
        reserve_3bot = content['reserve_3bot'] == 1
        videoconf = content['videoconf'] == 1
        social_media = content['social_media'] == 1
        farmer = content['farmer'] == 1
        deploy_it = content['deploy_it'] == 1
        gdpr = content['gdpr'] == 1
        cookies = content['cookies'] == 1
        email = content['email'] == 1
        user_secret = str(uuid.uuid1())
        cursor.execute("INSERT INTO users(email_address, secret, mobile, reserve_3bot, videoconf, social_media, farmer, deploy_it, gdpr, cookies, email) VALUES(?, ?, ?, ? ,?, ?, ?, ?, ?, ?, ?)",
                             [email_address,user_secret , mobile, reserve_3bot, videoconf, social_media, farmer, deploy_it, gdpr, cookies, email])
       
        print("User registered: ", email_address, uuid.uuid1(), mobile, reserve_3bot,
              videoconf, social_media, farmer, deploy_it, gdpr, cookies, email)

        con.commit()
        return user_secret


@app.route('/api/step2',  methods=['POST'])
def step2():
    con = db()
    email_address = ""
    secret = ""
    referral = False

    with con:
        cursor = con.cursor()
        content = request.get_json()
        secret = content['secret']
        referral = content['referral'] == 1
        currencies = content['currencies'] == 1

        cursor.execute("SELECT * FROM users where secret=?", [secret])
        user = cursor.fetchone()
        email_address = user[3] #todo map

        cursor.execute("UPDATE users SET referral=?, currencies=? WHERE secret=?",
                             [referral, currencies, secret])
        con.commit()

        if referral:
            # send email referral
            msg = email_referrer.get_email_referrer_text(secret)
            send_email.send_email(email_address,
                    email_referrer.get_email_referrer_subject(), msg)
            print("Send complete!")
        if currencies:
            # send email currencies
            print("not implemented")

    return "true"

#Add a referrer to db, someone that will refer other people
@app.route('/api/referral',  methods=['PUT'])
def add_referrer():
    con = db()
    with con:
        cursor = con.cursor()
        content = request.get_json()
        secret = content['secret']
        #get by secret
        referrer_email_address = content['referrer_email_address']
        cursor.execute("SELECT * FROM users where secret=?", [secret])
        user = cursor.fetchone()
        if user is None:
            return "User not found", 404
        #if users exists, add referral
        userId = user[0] #todo map
        cursor.execute("INSERT INTO referrers_user(userId, email_address) VALUES(?,?,?)", #this is just so the user can see who he invited already
                             [userId, referrer_email_address, 0])
        #send email
        msg = email_referred.get_email_referred_text(user[0])
        send_email.send_email(referrer_email_address,
                    email_referrer.get_email_referrer_subject(), msg)
        return ""


@app.route('/api/referral_done',  methods=['PUT'])
def update_referral():
    con = db()
    with con:
        cursor = con.cursor()
        content = request.get_json()
        #get by secret
        referral_email_address = content['referral_email_address']
        user_id = content['user_id']

        cursor.execute("SELECT * FROM users where id=?", [user_id])
        user = cursor.fetchone()
        if user is None:
            return "User not found", 404
        #if users exists, add referral
        
        cursor.execute("INSERT INTO referrals_done_user(userId, referral_email_address) VALUES(?,?,?)", #this is just so the user can see who he invited already
                             [user_id, referral_email_address])



def database_init():
    sql_user_entries = """ CREATE TABLE IF NOT EXISTS users (
                                        id INTEGER PRIMARY KEY,
                                        secret text NOT NULL,
                                        mobile text NOT NULL,
                                        email_address text NOT NULL,
                                        reserve_3bot integer NOT NULL,
                                        videoconf integer NOT NULL,
                                        social_media integer NOT NULL,
                                        farmer integer NOT NULL,
                                        deploy_it integer NOT NULL,
                                        gdpr integer NOT NULL,
                                        cookies integer NOT NULL,
                                        email integer NOT NULL,
                                        referral integer,
                                        currencies integer
                                    ); """

    sql_referrers_entries = """ CREATE TABLE IF NOT EXISTS referrers_user (
                                        id INTEGER PRIMARY KEY,
                                        userId INTEGER NOT NULL,
                                        email_address NOT NULL
                                    ); """
    #These referres have users that registered using the app and have points in the referral program
    sql_referrals_done_entries = """ CREATE TABLE IF NOT EXISTS referrals_done_user (
                                        id INTEGER PRIMARY KEY,
                                        userId INTEGER NOT NULL,
                                        referral_email_address NOT NULL
                                    ); """
    try:
        c = sqlite3.connect('calltoaction.db')
        c.execute(sql_user_entries)
        c.execute(sql_referrers_entries)
        c.execute(sql_referrals_done_entries)
        c.commit()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    database_init()
    app.run(debug=True)
