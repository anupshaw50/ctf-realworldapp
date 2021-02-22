# -*- coding: utf-8 -*-
from project import app
from project.models.Login import *
from flask import render_template, request, render_template_string, make_response, redirect, session
import uuid, hashlib, base64

@app.route("/login", methods=['GET'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    if not username:
        return render_template("login/index.html")
    else:
        u  = Users()
        values = u.login(username)
        if values:
            password_hash = hashlib.md5(str(password).encode("utf-8")).hexdigest()
            if values[0][3] == password_hash:
                session['userId'] = values[0][0]
                session['title'] = values[0][6]
                session['pic'] = values[0][4]
                session['loggedin'] = True
                session['username'] = username
                iv = "padding"                 
                csrf = username + iv
                session['csrf_token'] = base64.b64encode(csrf.encode())
                csrf_token = str(session['csrf_token'])
                return redirect("/dashboard/1", code=302)
            else:
                return render_template("login/index.html", error = "invalid password for username")
        else:
                return render_template("login/index.html", error = "invalid username")

