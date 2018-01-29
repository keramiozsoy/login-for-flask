from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import flash
import os

app = Flask(__name__)

@app.route("/")
def index():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('home.html')

@app.route("/login",methods=['POST'])
def login():
    if  request.form['username'] == 'test' and request.form['password'] == 'test' :
        session['logged_in'] = True
    else:
        flash('wrong password')

    return index()

#@app.route("/template")
#def template():
#    return render_template('template.html')

@app.route('/logout')
def logout():
    session['logged_inn'] = False
    return render_template('login.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(host='0.0.0.0',port=1111)
