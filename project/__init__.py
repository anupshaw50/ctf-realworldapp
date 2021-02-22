# -*- coding: utf-8 -*-
__version__ = '0.1'
from flask import Flask, request, Response, g, current_app
from datetime import datetime
import os
from flask_cors import CORS
import random
app = Flask('project')


app.config.update(dict(
    SECRET_KEY= "woopie",
    SESSION_COOKIE_HTTPONLY = False,
    DEBUG= True
))
#add this line in instances
cors = CORS(app, resources={r"/*": {"origins": "*"}})
@app.before_request
def before_request_func():
    url = request.url
    now = datetime.now()
    if("/static/" not in url and "/favicon.ico" not in url ):
        log = os.path.join(current_app.root_path, "static/log/log.txt")
        f = open(log, "a")
        val = str(request.values)
        fil = str(request.files)
        value_1 = val.replace("CombinedMultiDict([ImmutableMultiDict([]),","")
        value_2 = value_1.replace("ImmutableMultiDict([])","")
        final_val = value_2.replace("ImmutableMultiDict","")
        file_1 = fil.replace("CombinedMultiDict([ImmutableMultiDict([]),","")
        file_2 = file_1.replace("ImmutableMultiDict([])","")
        final_file = file_2.replace("ImmutableMultiDict","")
        f.write(str(request.remote_addr)+" - "+"["+str(now)+"] - "+str(request.method)+" "+str(request.url)+" - "+str(final_val)+" "+str(final_file)+"\r\n")
        f.close()

from project.controllers import *

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
    app.run(debug=True)

