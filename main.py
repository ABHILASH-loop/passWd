from flask import Flask, render_template, request,  url_for, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates', static_url_path='/static')
app.static_folder = 'static'
app.secret_key = "nothing"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///USER.sqlite3'

db = SQLAlchemy(app)


class userDetail(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("Username", db.String(100))
    email = db.Column("email", db.String(100))
    passwd = db.Column("passwd", db.String(10))

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


def checkMail(email):
    a = [x[0] for x in userDetail.query.with_entities(userDetail.email)]
    if email in a:
        return True
    return False

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        if request.form["popup"]:
            return redirect(url_for(
                "webDetails",
                webs_id=request.form["popup"],
            ))
            
    btn_datas = list(db.session.query(webInfo._id, webInfo.web_name))

    return render_template("home.html", webs=btn_datas, show="False")


@app.route("/webdetails", methods=["GET", "POST"])
def webDetails():
    
    if request.method == "POST":
        print('HI ....')
        if request.form["submit"]:
            print('HI ....')
            
    id = int(request.args.get('webs_id'))
    datas = webInfo.query.filter_by(_id=id).first()

    if id == 0:
        return render_template(
            "info_popup.html",
            data=["Enter Website name", "", ""],
            show="True",
            submit="Save",
            disable="True",
            placeholder=["User ID", "passWd"]
        )
    elif id > 0:
        return render_template(
            "info_popup.html",
            data=[datas.web_name, datas.user_id, datas.passwd],
            show="True",
            submit="Close",
            disable="False",
            placeholder="  "
        )

@app.route("/addDetails")
def addDetails():
    web_name, user_id, passwd = request.args.get("web_name"), request.args.get("user_id"), request.args.get("passwd")
    print(web_name, user_id, passwd)
    return redirect(url_for('home'))
"""     if request.form["submit"]:
                web_name = request.form.get("webname")
                user_id = request.form.get("userid")
                passwd = request.form.get("passwd")
                datas = webInfo(web_name, user_id, passwd)
                print("true", web_name, user_id) """

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        if request.form['signup'] == 'tosignup':
            return redirect(url_for("signup"))
    return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == 'POST':
        username = request.form.get("name")
        email = request.form.get("email")
        passwd = request.form.get("passwd")

        datas = userDetail(username, email, passwd)
        if datas.query.filter_by(email=email).first():
            return render_template("user_exsist.html", email=email)
        else:
            db.session.add(datas)
            db.session.commit()
            return render_template("OTP.html", email=email)
    return render_template("signup.html")


if __name__ == "__main__":
    ''' db.session.query(userDetail).delete()
    db.session.commit() '''

    db.create_all()
    app.run(debug=True)
