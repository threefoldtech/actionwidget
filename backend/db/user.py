from db import get_db


class User:
    def __init__(self, id, email_address,referrer_token, verify_token, host_3bot_name, mobile, reserve_3bot, videoconf, social_media, farmer, deploy_it, gdpr, cookies, email, referral = False, currencies = False, verified = False):
        self.id = id
        self.email_address = email_address
        self.referrer_token = referrer_token
        self.verify_token = verify_token
        self.mobile = mobile
        self.reserve_3bot = reserve_3bot
        self.videoconf = videoconf
        self.social_media = social_media
        self.farmer = farmer
        self.deploy_it = deploy_it
        self.gdpr = gdpr
        self.cookies = cookies
        self.email = email
        self.referral = referral
        self.currencies = currencies
        self.verified = verified
        self.host_3bot_name = host_3bot_name
    def add(self):
        if self.id is not 0:
            return False #maybe except?

        con = get_db()
        cursor = con.cursor()
        with con:
            cursor.execute("INSERT INTO users(email_address, referrer_token, verify_token, host_3bot_name, mobile, reserve_3bot, videoconf, social_media, farmer, deploy_it, gdpr, cookies, email, referral, currencies, verified) VALUES(?, ?, ?, ? ,?, ?, ?, ?, ?, ?, ?, ?, ?,?,?,?)",
                             [self.email_address, self.referrer_token, self.verify_token, self.host_3bot_name, self.mobile, self.reserve_3bot, self.videoconf, self.social_media, self.farmer, self.deploy_it, self.gdpr, self.cookies, self.email, self.referral, self.currencies, self.verified])
        self.id = cursor.lastrowid
        print("User registered: ", self.email_address, self.referrer_token, self.verify_token, self.host_3bot_name, self.mobile,  self.reserve_3bot, self.videoconf, self.social_media, self.farmer, self.deploy_it, self.gdpr, self.cookies, self.email, self.referral, self.currencies, self.verified)
        return True

    def update(self):
        if self.id is 0:
            return False #maybe except?

        con = get_db()
        cursor = con.cursor()
        with con:
            cursor.execute("UPDATE users SET email_address=?, referrer_token=?, verify_token=?, host_3bot_name=?, mobile=?, reserve_3bot=?, videoconf=?, social_media=?, farmer=?, deploy_it=?, gdpr=?, cookies=?, email=?, referral=?, currencies=?, verified=? where id = ?",
                             [self.email_address, self.referrer_token, self.verify_token, self.host_3bot_name, self.mobile, self.reserve_3bot, self.videoconf, self.social_media, self.farmer, self.deploy_it, self.gdpr, self.cookies, self.email, self.referral, self.currencies, self.verified, self.id])

        print("User updated: ", self.email_address, self.referrer_token, self.verify_token, self.host_3bot_name, self.mobile,  self.reserve_3bot, self.videoconf, self.social_media, self.farmer, self.deploy_it, self.gdpr, self.cookies, self.email, self.referral, self.currencies, self.verified)
        return True

    @classmethod
    def get_by_referrer_token(cls, token):
        con = get_db()
        cursor = con.cursor()
        with con:
            cursor.execute("SELECT * FROM users where referrer_token=?", [token])
            entry = cursor.fetchone()
            if entry is None:
                return entry
            return cls(entry[0],entry[1],entry[2],entry[3],entry[4],entry[5],entry[6],entry[7],entry[8],entry[9],entry[10], entry[11], entry[12], entry[13], entry[14])
    
    @classmethod
    def get_by_verify_token(cls, token):
        con = get_db()
        cursor = con.cursor()
        with con:
            cursor.execute("SELECT * FROM users where verify_token=?", [token])
            entry = cursor.fetchone()
            if entry is None:
                return entry
            return cls(entry[0],entry[1],entry[2],entry[3],entry[4],entry[5],entry[6],entry[7],entry[8],entry[9],entry[10], entry[11], entry[12], entry[13], entry[14])
    
    @classmethod
    def get_by_id(cls, id):
        con = get_db()
        cursor = con.cursor()
        with con:
            cursor.execute("SELECT * FROM users where id=?", [id])
            entry = cursor.fetchone()
            if entry is None:
                return entry
            return cls(entry[0],entry[1],entry[2],entry[3],entry[4],entry[5],entry[6],entry[7],entry[8],entry[9],entry[10], entry[11], entry[12], entry[13], entry[14])
    
    @classmethod
    def get_by_email_address(cls, email_address):
        print(cls)
        con = get_db()
        cursor = con.cursor()
        with con:
            cursor.execute("SELECT * FROM users where email_address=?", [email_address])
            entry = cursor.fetchone()
            if entry is None:
                return entry
            return cls(entry[0],entry[1],entry[2],entry[3],entry[4],entry[5],entry[6],entry[7],entry[8],entry[9],entry[10], entry[11], entry[12], entry[13], entry[14])
