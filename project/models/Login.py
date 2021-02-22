from project.config.sqlite import *

class Users:
    
    def login(self, username):
	    db = database_con()
	    cur = db.execute('SELECT * FROM users WHERE UserName=?',[username])
	    return cur.fetchall()