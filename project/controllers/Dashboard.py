# -*- coding: utf-8 -*-
from project import app
from project.models.Dashboard import *
from flask import render_template, request, render_template_string, redirect


@app.route("/dashboard/<pageId>", methods=['GET'])
def inject(pageId):
    if pageId == 0:
        pageId = 1
    sqli  = Dashboard()
    values = sqli.getPage(pageId)
    title   = values[0][0]
    content = values[0][1]
    return render_template("dashboard/index.html",title = title, content = content, id = id)


@app.route("/", methods=['GET'])
def router():
    return redirect("/dashboard/1", code=302)