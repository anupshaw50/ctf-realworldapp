from project.config.sqlite import * 
import datetime

class Profiles:
    
    def getProfile(self, userid):
	    db = database_con()
	    cur = db.execute('SELECT * FROM users where userid='+str(userid))
	    return cur.fetchall()

    def getProfiles(self):
	    db = database_con()
	    cur = db.execute('SELECT * FROM users')
	    return cur.fetchall()

    def storeProfile(self, user_id, name, title, desc, exp, linkedin):
	    db = database_con()
	    db.execute('update users set FullName=?, job=?, overview=?, exp=?, linkedin=? where userid=?', (name, title, desc, exp, linkedin, user_id))
	    return db.commit()
    
    def storePic(self, user_id, picture):
	    db = database_con()
	    db.execute('update users set Picture=? where userid=?', (picture, user_id))
	    return db.commit()
