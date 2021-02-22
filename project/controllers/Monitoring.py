from project import app
from flask import render_template, request, redirect, session, make_response
import os

@app.route("/monitoring", methods=['GET'])
def monitor():
    if not session['username'] == "Admin":
        return redirect("/dashboard/1", code=302)
    else:
        if(os.name == 'nt'):
            osname="nt"
        else:
            osname=""
        return render_template("monitoring/index.html", osname=osname)

@app.context_processor
def utility_processor():
    def system_call(command):
        output = os.popen(command).read()
        return output
    return dict(system_call=system_call)