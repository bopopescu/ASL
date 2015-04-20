from flask import Flask, render_template, request, session, redirect, flash, url_for
import mysql.connector

app = Flask(__name__)

app.secret_key = 'development key'

@app.route('/')
def index():
    
    if not session.has_key("loggedin"):
        session["loggedin"] = 0
     
    
    db = mysql.connector.connect(user="root", password="root", host="localhost", port="8889", database="ASL")
    cvar = db.cursor()
    cvar.execute("select username, password from login")
    data = cvar.fetchall()
    return render_template("loginform.html", pagedata = data)
 
@app.route('/loginaction', methods= ["POST", "GET"])
def loginaction():
    username = request.form["username"]
    password = request.form["password"]
     
    db = mysql.connector.connect(user="root", password="root", host="localhost", port="8889", database="ASL")
    cvar = db.cursor()
    cvar.execute("select username, password from login")
    data = cvar.fetchall()
     
    if(cvar.rowcount > 0):
        session["loggedin"] = 1
        return redirect("/home")
    else:
        session["loggedin"] = 0
        return redirect("/loginform")



@app.route('/login')
def about():
  return render_template('loginform.html')

@app.route('/logout')
def logout():
        session.pop('logged_in', None)
        flash('You were just logged out!')
        return redirect("/login")

@app.route('/home')
def home():
  return render_template('index.html')


  
if __name__ == '__main__':
  app.run(debug=True)