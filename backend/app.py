
import sqlite3
from flask import Flask
from flask import request
from validate_email import validate_email
import send_email
import email_referral
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
        email_address = content['email_address']
        if not validate_email(email_address):
            return "Email address invalid", 400
        mobile = content['mobile']
        reserve_3bot = content['reserve_3bot'] == 1
        videoconf = content['videoconf'] == 1
        social_media = content['social_media'] == 1
        farmer = content['farmer'] == 1
        deploy_it = content['deploy_it'] == 1
        gdpr = content['gdpr'] == 1
        cookies = content['cookies'] == 1
        email = content['email'] == 1
        print(email_address, uuid.uuid1(), mobile, reserve_3bot,
              videoconf, social_media, farmer, deploy_it, gdpr, cookies, email)
        con.cursor().execute("INSERT INTO users(email_address, secret, mobile, reserve_3bot, videoconf, social_media, farmer, deploy_it, gdpr, cookies, email) VALUES(?, ?, ?, ? ,?, ?, ?, ?, ?, ?, ?)",
                             [email_address, str(uuid.uuid1()), mobile, reserve_3bot, videoconf, social_media, farmer, deploy_it, gdpr, cookies, email])
        con.commit()
        return str(uuid.uuid1())


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
            msg = email_referral.get_email_referral_text(secret)
            send_email.send_email(email_address,
                    email_referral.get_email_referral_subject(), msg)
            print("Send complete!")
        if currencies:
            # send email currencies
            print("not implemented")

    return "true"


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
    try:
        c = sqlite3.connect('calltoaction.db')
        c.execute(sql_user_entries)
        c.commit()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    database_init()
    app.run(debug=True)
