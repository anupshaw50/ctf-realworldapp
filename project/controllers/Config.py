# -*- coding: utf-8 -*-

from project import app
from project.models.Dashboard import *
from flask import render_template, request
import pickle
from io import StringIO  # Python3
import sys
import yaml
import base64

@app.route("/config/<input>", methods=['GET'])
def config_input(input): 
    #try: 
    if not input:
        return render_template("config/index.html")
    yaml_file = base64.b64decode(input)
    content = yaml.load(yaml_file)
    return render_template("config/index.html", content = content['sudo'], msg="The server configuration has been restored to the original key 'sudo' with value: ")
    
@app.route("/config", methods=['GET'])
def config(): 
    return render_template("config/index.html" , content = "", msg="")