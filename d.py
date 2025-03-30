from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_pymongo import PyMongo
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(name)
app.config['SECRET_KEY'] = 'your_secret_key'  #ttt
app.config["MONGO_URI"] = "mongodb://localhost:27017/your_db"  
mongo = PyMongo(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

class User(UserMixin):
    def init(self, username, user_id):
        self.id = user_id
        self.username = username

@login_manager.user_loader
def load_user(user_id):
    user = mongo.db.users.find_one({"_id": user_id})
    if user:
        return User(user['username'], str(user['_id']))
    return None

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = mongo.db.users.find_one({"username": username})
        if user and user["password"] == password:
            user_obj = User(username, str(user['_id']))
            login_user(user_obj)
            return redirect(url_for("profile"))

        flash("Invalid credentials. Please try again.")
        return redirect(url_for("login"))

    return render_template("login.html")

@app.route("/profile")
@login_required
def profile():
    return render_template("profile.html", username=current_user.username)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

if name == "main":
    app.run(debug=True)