from db import get_db


class User:
    def __init__(self, id, email_address,name):
        self.id = id
        self.email_address = email_address
        self.name = name

    def add(self):
        if self.id is not 0:
            return False #maybe except?

        con = get_db()
        cursor = con.cursor()
        with con:
            cursor.execute("INSERT INTO users(email_address, name) VALUES(?, ?)",
                             [self.email_address, self.name])
        self.id = cursor.lastrowid
        print("User registered: ", self.email_address, self.name)
        return True

    def update(self):
        if self.id is 0:
            return False #maybe except?

        con = get_db()
        cursor = con.cursor()
        with con:
            cursor.execute("UPDATE users SET email_address=?, name=? where id = ?",
                             [self.email_address, self.name, self.id])

        print("User updated: ", self.id, self.email_address, self.name)
        return True

    
    @classmethod
    def get_by_id(cls, id):
        con = get_db()
        cursor = con.cursor()
        with con:
            cursor.execute("SELECT * FROM users where id=?", [id])
            entry = cursor.fetchone()
            if entry is None:
                return entry
            return cls(entry[0],entry[1],entry[2])
    
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
            return cls(entry[0],entry[1],entry[2])
    @classmethod
    def get(cls):
        referrals = []
        con = get_db()
        cursor = con.cursor()
        
        with con:
            cursor.execute("SELECT * FROM users")
            for row in cursor:
                referrals.append(cls(row[0], row[1], row[2]))
            return referrals