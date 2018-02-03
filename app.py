from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import flash
import os

from peewee import *

app = Flask(__name__)

db = SqliteDatabase('test.db')


@app.route("/")
def index():
    records = Person.select()

    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('home.html',result=records)

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

class Person(Model):
    name = CharField()
    surname = CharField()
    active = BooleanField()

    class Meta:
        database = db


		
class Pet(Model):
    person = ForeignKeyField(Person, related_name='pets')
    petName = CharField()

    class Meta:
        database = db

db.connect()

if not (
	Person.table_exists() and Pet.table_exists()
):
	db.create_tables([Person,Pet])


testData = Person(name='Kerami',surname='Ozsoy',active=True)
testData.save()

testData2 = Person(name='TestName',surname='TestSur',active=False)
testData2.save()

testData3 = Pet(person=testData,petName='kopek')
testData3.save()

db.close()


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(host='0.0.0.0',port=1111)
