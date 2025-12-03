from flask import Flask,redirect,session,url_for,flash,render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "akshitrana"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFIACTIONS"] = False

db = SQLAlchemy(app)

class data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)


with app.app_context():
    db.create_all()


@app.route("/",methods=["POST","GET"])
def homepage():
    if request.method == "GET":
        return render_template("base.html")
    

@app.route("/contact",methods=["GET","POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html")
    


    
@app.route("/details",methods=["GET","POST"])
def details():
    if request.method == "GET":
        return render_template("details.html")
    

    
@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "POST":
        user = request.form.get("username")
        pas = request.form.get("password")

        check_user = data.query.filter_by(name=user,password=pas).first()

        if check_user:
            return redirect(url_for("thankyou"))
        
        else:
            return redirect(url_for("login"))
        
    return render_template("login.html")


    

@app.route("/signup",methods=["GET","POST"])
def signup():
    if request.method == "POST":
        user = request.form.get("username")
        pas = request.form.get("password")

        id = data(name=user,password=pas)
        db.session.add(id)
        db.session.commit()
        return redirect(url_for("login"))
    
    return render_template("signup.html")



@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")
    

