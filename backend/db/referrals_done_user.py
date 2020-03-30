from db import get_db
import sqlite3
import json

class Referrals_Done_User:
    def __init__(self, id, user_id, referral_email_address):
        self.id = id
        self.user_id = user_id #user by whom referred
        self.referral_email_address = referral_email_address
      
    def add(self):
        if self.id is not 0:
            return False #maybe except?

        con = get_db()
        cursor = con.cursor()
        with con:
            cursor.execute("INSERT INTO referrals_done_user(user_id, referral_email_address) VALUES(?, ?)",
                             [self.user_id, self.referral_email_address])
        self.id = cursor.lastrowid
        print("referrals_done_user added: ", self.id ,self.user_id, self.referral_email_address)
        return True
    
    def update(self):
        if self.id is 0:
            return False #maybe except?

        con = get_db()
        cursor = con.cursor()
        with con:
            cursor.execute("UPDATE referrals_done_user SET user_id=?, referral_email_address=? where id = ?",
                             [self.user_id, self.referral_email_address, self.id])

        print("referrals_done_user updated: ", self.id, self.user_id, self.referral_email_address)
        return True

        
    def to_json(self):
        jsonobj = {}
        jsonobj['user_id'] = self.user_id
        jsonobj['referral_email_address'] = self.referral_email_address
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
            cursor.execute("SELECT * FROM referrals_done_user where referral_email_address=?", [email_address])
            entry = cursor.fetchone()
            return entry is not None #false is good

