from project.config.sqlite import * 

class Dashboard:
    
    def getPage(self, pageId):
	    db = database_con()
	    cur = db.execute('SELECT title, content FROM pages WHERE pageId=?',(pageId, ))
	    return cur.fetchall()
    
