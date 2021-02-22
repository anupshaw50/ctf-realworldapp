# -*- coding: utf-8 -*-
from project import app
from project.models.Dashboard import *
from flask import render_template, request, render_template_string, make_response


@app.route("/search", methods=['GET', 'POST'])
def xss_level_1():
    search = request.form.get('search')
    r = make_response(render_template("search/index.html", search = search))
    r.headers.set('X-XSS-Protection', '0')
    return r
