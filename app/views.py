from flask import render_template
from app import app
import geoparser.geomjsonparser as parser

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/dronemap')
def dronemap():
    return render_template('dronemap.html', shapes)
