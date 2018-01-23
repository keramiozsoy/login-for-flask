from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login",methods=['POST'])
def login():
    if  request.form['username'] == 'test' and request.form['password'] == 'test' :
      return render_template('home.html')
    else:
      return index()

@app.route("/template")
def template():
    return render_template('template.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=1111)
