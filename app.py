from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import redirect # I will learn after that will use
from flask import url_for  # I will learn after that will use
from flask import flash    # I will learn after that will use
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
    if  request.method == 'POST':
        user_name = request.form['username']
        sur_name = request.form['password']
        login_user = Person.select().where(Person.name == user_name, Person.surname == sur_name)
        if login_user.exists():
            session['logged_in'] = True
            session['username'] = user_name
            session['password'] = sur_name
            return render_template('home.html')
        else:
            return render_template('login.html')
    else:
        return render_template('login.html')

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
	db.create_tables([Person,Pet], safe=True)


testData = Person(name='Kerami',surname='Ozsoy',active=True)
testData.save()

testData2 = Person(name='test',surname='test',active=False)
testData2.save()

testData3 = Pet(person=testData,petName='dog')
testData3.save()

db.close()


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(host='0.0.0.0',port=1111)
