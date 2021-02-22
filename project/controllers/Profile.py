from project import app
from project.models.Profiles import *
from flask import render_template, request, redirect, session, make_response
import uuid, os

@app.route("/profile", methods=['GET'])
def profile():
    try:
        sqli  = Profiles()
        user_prof = sqli.getProfile(session['userId'])
        user_id = user_prof[0][0]
        username = user_prof[0][1]
        name = user_prof[0][2]
        pic = user_prof[0][4]
        banner = user_prof[0][5]
        title = user_prof[0][6]
        desc = user_prof[0][7]
        exp = user_prof[0][8]
        linkedin = user_prof[0][9]
        return render_template("profile/index.html", username = username, name=name, pic=pic, banner=banner, title=title, exp=exp, linkedin=linkedin, desc=desc, user_id=user_id)
    except:
        return redirect("/login", code=302)

@app.route("/profile/all", methods=['GET'])
def profiles():
        sqli  = Profiles()
        users_prof = sqli.getProfiles()
        return render_template("profile/all.html", users_prof = users_prof)

@app.route("/profile/<id>", methods=['GET'])
def profile_id(id):
        sqli  = Profiles()
        user_prof = sqli.getProfile(id)
        user_id = user_prof[0][0]
        username = user_prof[0][1]
        name = user_prof[0][2]
        pic = user_prof[0][4]
        banner = user_prof[0][5]
        title = user_prof[0][6]
        desc = user_prof[0][7]
        exp = user_prof[0][8]
        linkedin = user_prof[0][9]
        return render_template("profile/index.html", username = username, name=name, pic=pic, banner=banner, title=title, exp=exp, linkedin=linkedin, desc=desc, user_id=user_id)
 
@app.route("/profile/edit", methods=['GET', 'POST'])
def profile_edit():
    try:
        sqli  = Profiles()
        user_prof = sqli.getProfile(session['userId'])
        user_id = user_prof[0][0]
        username = user_prof[0][1]
        name = user_prof[0][2]
        pic = user_prof[0][4]
        banner = user_prof[0][5]
        title = user_prof[0][6]
        desc = user_prof[0][7]
        exp = user_prof[0][8]
        linkedin = user_prof[0][9]
        return render_template("profile/edit.html", username = username, name=name, pic=pic, banner=banner, title=title, exp=exp, linkedin=linkedin, desc=desc, user_id=user_id)
    except:
        return redirect("/login", code=302)

@app.route("/profile/update", methods=['GET', 'POST'])
def profile_update():
    try:
        name = request.form['name']
        title = request.form['title']
        desc = request.form['desc']
        exp = request.form['exp']
        linkedin = request.form['linkedin']
        sqli  = Profiles()
        user_prof = sqli.storeProfile(session['userId'], name, title, desc, exp, linkedin)
        return redirect("/profile", code=302)
    except:
        return render_template("profile/index.html")

@app.route("/profile/uploads", methods=['POST'])
def profile_uploads():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = file.filename
            file.save(os.path.join('project/static/images/', filename))
            uploaded = "File was uploaded succesfully to the application."
            sqli  = Profiles()
            user_prof = sqli.storePic(session['userId'], filename)
            return render_template("profile/edit.html", uploaded = uploaded , username ="", name="", pic="", banner="", title="", exp="", linkedin="", desc="")
        uploaded = "something went wrong, please try again. If the problem is repetitive please contact an administrator!"
        return render_template("profile/edit.html", uploaded = uploaded , username ="", name="", pic="", banner="", title="", exp="", linkedin="", desc="")
    return render_template("profile/edit.html")