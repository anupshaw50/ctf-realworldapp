from project import app
from flask import render_template, request

@app.route("/list", methods=['GET'])
def list():
    return render_template("construction/list.txt")

