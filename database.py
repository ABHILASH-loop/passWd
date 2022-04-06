from flask import Flask, render_template, request, url_for, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "nothing"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///USER.sqlite3'

db = SQLAlchemy(app)

class userDetail(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("Username", db.String(100))
    email = db.Column("email", db.String(100))
    passwd = db.Column("passwd", db.String(15))
    
    def __init__(self, name, email, passwd):
        self.name = name
        self.email = email
        self.passwd = passwd

class webInfo(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    web_name = db.Column("webName", db.String(20))
    user_id = db.Column("user_id", db.String(30))
    passwd = db.Column("passwd", db.String(15))
    
    def __init__(self, web_name, user_id, passwd):
        self.web_name = web_name
        self.user_id = user_id
        self.passwd = passwd

""" datas = webInfo("Abhilash", "c", "1234@")
db.session.add(datas) """

""" db.session.query(webInfo).delete() """
webInfo.query.filter_by(_id=3).delete()

db.session.commit()

db.create_all()