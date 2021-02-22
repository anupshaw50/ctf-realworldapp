# -*- coding: utf-8 -*-
from project import app
from project.models.Dashboard import *
from flask import render_template, request, render_template_string, redirect, make_response, send_file
from xml.dom import minidom
from xml.dom.pulldom import parse
from xml.sax import make_parser
from xml.sax.handler import feature_external_ges
from xml.dom.pulldom import START_ELEMENT, parseString

@app.route("/companies", methods=['GET'])
def companies():
    return render_template("companies/index.html")


@app.route("/companies/new", methods=['GET'])
def add_company():
    return render_template("companies/new.html")


@app.route("/companies/getXML", methods=['GET', 'POST'])
def XML_template():
    fileName = request.form['company']
    file = open(fileName)
    response = make_response(send_file(fileName, attachment_filename=fileName))
    response.headers.set("Content-Type", "text/html; charset=utf-8")
    response.headers.set("Content-Disposition", "attachment; filename="+fileName)
    return response


@app.route("/company/upload", methods=['POST'])
def company_upload():
    parser = make_parser()
    parser.setFeature(feature_external_ges, True)
    file = request.files['company']
    filename = file.filename
    file.save(filename)
    doc = parse(filename, parser=parser)
    try:
        for event, node in doc:
            if event == START_ELEMENT and node.localName == "data":
                doc.expandNode(node)
                nodes = node.toxml()
                return render_template("companies/new.html", nodes = nodes)
    except:
        return render_template("companies/new.html", error = "Validation failed")
    return render_template("companies/new.html", error = "Validation failed")