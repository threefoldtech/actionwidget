import sqlite3
import db

def get_db():
    db_api = sqlite3.connect('calltoaction.db')
    
    return db_api


def init():
    print("Initializing db")
    sql_referrers_entries = """ CREATE TABLE IF NOT EXISTS referrals_pending_user (
                                    id INTEGER PRIMARY KEY,
                                    user_id INTEGER NOT NULL,
                                    email_address NOT NULL
                                ); """
    #These referres have users that registered using the app and have points in the referral program
    sql_referrals_done_entries = """ CREATE TABLE IF NOT EXISTS referrals_done_user (
                                    id INTEGER PRIMARY KEY,
                                    user_id INTEGER NOT NULL,
                                    referral_3bot_name NOT NULL
                                ); """

    sql_user_entries = """ CREATE TABLE IF NOT EXISTS users (
                                    id INTEGER PRIMARY KEY,
                                    email_address text NOT NULL,
                                    referrer_token text NOT NULL,
                                    verify_token text NOT NULL,
                                    mobile text NOT NULL,
                                    reserve_3bot integer NOT NULL,
                                    videoconf integer NOT NULL,
                                    social_media integer NOT NULL,
                                    farmer integer NOT NULL,
                                    deploy_it integer NOT NULL,
                                    gdpr integer NOT NULL,
                                    cookies integer NOT NULL,
                                    email integer NOT NULL,
                                    referral integer,
                                    currencies integer,
                                    verified integer
                                ); """



    try:
        c = sqlite3.connect('calltoaction.db')
        c.execute(sql_user_entries)
        c.execute(sql_referrers_entries)
        c.execute(sql_referrals_done_entries)
        c.commit()
        print("db initialized")
    except Exception as e:
        print(e)