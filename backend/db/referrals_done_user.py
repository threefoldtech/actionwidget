from db import get_db
import sqlite3
import json

class ReferralsDoneUser:
    def __init__(self, id, user_id, referral_3bot_name):
        self.id = id
        self.user_id = user_id #user by whom referred
        self.referral_3bot_name = referral_3bot_name
      
    def add(self):
        if self.id is not 0:
            return False #maybe except?

        con = get_db()
        cursor = con.cursor()
        with con:
            cursor.execute("INSERT INTO referrals_done_user(user_id, referral_3bot_name) VALUES(?, ?)",
                             [self.user_id, self.referral_3bot_name])
        self.id = cursor.lastrowid
        print("referrals_done_user added: ", self.id ,self.user_id, self.referral_3bot_name)
        return True
    
    def update(self):
        if self.id is 0:
            return False #maybe except?

        con = get_db()
        cursor = con.cursor()
        with con:
            cursor.execute("UPDATE referrals_done_user SET user_id=?, referral_3bot_name=? where id = ?",
                             [self.user_id, self.referral_3bot_name, self.id])

        print("referrals_done_user updated: ", self.id, self.user_id, self.referral_3bot_name)
        return True

        
    def to_json(self):
        jsonobj = {}
        jsonobj['user_id'] = self.user_id
        jsonobj['referral_3bot_name'] = self.referral_3bot_name
        return jsonobj
        
    @classmethod
    def get(cls, user_id):
        referrals = []
        con = get_db()
        cursor = con.cursor()
        
        with con:
            cursor.execute("SELECT * FROM referrals_done_user where user_id=?", [user_id])
            for row in cursor:
                referrals.append(cls(row[0], row[1], row[2]))
            return referrals
            
    @staticmethod
    def check_already_referred_email_address(email_address):
        con = get_db()
        cursor = con.cursor()
        with con:
            cursor.execute("SELECT * FROM referrals_done_user where referral_3bot_name=?", [email_address])
            entry = cursor.fetchone()
            return entry is not None #false is good

