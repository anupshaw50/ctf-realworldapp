from project import app
from flask import render_template, request

@app.route("/construction", methods=['GET'])
def construction():
    return render_template("construction/index.html")

