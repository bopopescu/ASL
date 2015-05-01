from flask import Flask, session, request, render_template, redirect, jsonify, flash, url_for
import os,mysql.connector, json, urllib
from flask_wtf import Form
from wtforms.fields.html5 import DateField

app = Flask(__name__)
secret_key = 'routes'


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/apiform')
def apiform():
    return render_template('apiform.html')
 
@app.route('/apiresponse', methods=['POST','GET'])
def apiresponse():
    year = request.form['year']
    url = "https://api.sportsdatallc.org/mlb-t5/seasontd/2015/reg/standings.json?api_key=teude223ssfsj25rbu4dpgmx"
    url2 = "https://api.sportsdatallc.org/mlb-t5/seasontd/2015/reg/leaders/statistics.json?api_key=teude223ssfsj25rbu4dpgmx"
    loadurl = urllib.urlopen(url)
    loadurl2 = urllib.urlopen(url2)
 
    data1 = json.loads(loadurl.read().decode(loadurl.info().getparam('charset')or'utf-8'))
    data2 = json.loads(loadurl2.read().decode(loadurl2.info().getparam('charset')or'utf-8'))
    data = (data1,data2)
 
    return render_template('apiform.html',pagedata=data)

@app.route('/apirosters')
def apirosters():
    return render_template('rosters.html')
 
@app.route('/rostersresponse', methods=['POST','GET'])
def rostersresponse():
    year = request.form['year']
    url = "http://api.sportradar.us/mlb-t5/games/2015/04/30/schedule.json?api_key=teude223ssfsj25rbu4dpgmx"
    url2 = "http://api.sportradar.us/mlb-t5/league/venues.json?api_key=teude223ssfsj25rbu4dpgmx"
    loadurl = urllib.urlopen(url)
    loadurl2 = urllib.urlopen(url2)
 
    data1 = json.loads(loadurl.read().decode(loadurl.info().getparam('charset')or'utf-8'))
    data2 = json.loads(loadurl2.read().decode(loadurl2.info().getparam('charset')or'utf-8'))
    data = (data1,data2)
 
    return render_template('rosters.html',pagedata=data)

if __name__ == '__main__':
  app.run(debug=True)