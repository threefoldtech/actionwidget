from db import get_db


class Referrals_Pending_User:
    def __init__(self, id, user_id, email_address):
        self.id = id
        self.user_id = user_id #user by whom referred
        self.email_address = email_address
      
    def add(self):
        if self.id is not 0:
            return False #maybe except?

        con = get_db()
        cursor = con.cursor()
        with con:
            cursor.execute("INSERT INTO referrals_pending_user(user_id, email_address) VALUES(?, ?)",
                             [self.user_id, self.email_address])
        self.id = cursor.lastrowid
        print("referrals_pending_user added: ", self.id ,self.user_id, self.email_address)
        return True

    @classmethod
    def get(cls, user_id):
        referrals = []
        con = get_db()
        cursor = con.cursor()
        
        with con:
            cursor.execute("SELECT * FROM referrals_pending_user where user_id=?", [user_id])
            for row in cursor:
                referrals.append(cls(row[0], row[1], row[2]))
            return referrals
    
    def to_json(self):
        jsonobj = {}
        jsonobj['user_id'] = self.user_id
        jsonobj['email_address'] = self.email_address
        return jsonobj
        
    def update(self):
        if self.id is 0:
            return False #maybe except?

        con = get_db()
        cursor = con.cursor()
        with con:
            cursor.execute("UPDATE referrals_pending_user SET user_id=?, email_address=? where id = ?",
                             [self.user_id, self.email_address, self.id])

        print("User updated: ", self.id, self.user_id, self.email_address)
        return True