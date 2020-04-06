import sqlite3
import db

def get_db():
    db_api = sqlite3.connect('calltoaction.db')
    
    return db_api


def init():
   

    sql_user_entries = """ CREATE TABLE IF NOT EXISTS users (
                                    id INTEGER PRIMARY KEY,
                                    email_address text NOT NULL,
                                    name text NOT NULL
                                ); """



    try:
        c = sqlite3.connect('calltoaction.db')
        c.execute(sql_user_entries)
        c.commit()
        print("db initialized")
    except Exception as e:
        print(e)