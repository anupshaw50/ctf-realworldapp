#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, random
from project import app
from flask_cors import CORS

app.config.update(dict(
    SECRET_KEY= "woopie",
    SESSION_COOKIE_HTTPONLY = False,
    DEBUG= True
))
  
if __name__ == '__main__':
    cors = CORS(app, resources={r"/*": {"origins": "*"}})
    try:
        f=open("project/static/source/code.zip")
        print("file is there")
        # Do something with the file
    except IOError:
        print("First startup")
        ran = random.randint(0,9)
        if(ran <= 5):
            os.system("cp random/sql/Profiles.py project/models")
        else:
            os.system("cp random/sql/Dashboard.py project/models")
        os.system("rm -rf random/sql")
        os.system("zip -r project/static/source/code.zip ../target")
    app.run(host='0.0.0.0',port=8000)

