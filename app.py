from flask import render_template, redirect, url_for, Flask, session, request
import os
from datetime import datetime
from helpers.auth import login_required, login_function
from helpers.posts import add_new_post, delete_post, update_post, load_posts
import secrets  # used to make a secret token which the flask app uses for data retrieval
from dotenv import load_dotenv
from flask_session import Session

load_dotenv()


app = Flask(__name__)

app.secret_key = os.environ.get("SECRET_KEY")


@app.route("/")
def home():
    title = "Roadmap.sh Blog"
    posts = load_posts()
    return render_template("pages/home.html", title=title, posts=posts)


@app.route("/admin", methods=["GET", "POST"])
def admin():
    if session.get("admin_id"):
        return redirect(url_for("dashboard"))
    title = "Admin Login"
    if request.method == "POST":
        username = request.form.get("username").strip()
        password = request.form.get("password").strip()
        login = login_function(username, password)
        if login == True:
            session.clear()
            session["admin_id"] = 1
            session.modified = True
            session.permanent = True
            return redirect(url_for("dashboard"))
        else:
            return "Username or Password Incorrect!", 400
    return render_template("pages/admin/admin.html", title=title)


@app.route("/logout")
@login_required
def logout():
    session.clear()
    session.modified = True
    return redirect(url_for("home"))


@app.route("/add_post", methods=["POST", "GET"])
@login_required
def add_post():
    title = "Add Post"
    if request.method == "POST":
        title = request.form.get("title").strip().title()
        description = request.form.get("description").strip()
        content = request.form.get("content").strip()
        time = datetime.now().replace(microsecond=0)
        try:
            add_new_post(title, description, content, time)
        except Exception as e:
            return f"{e}", 400
        return redirect(url_for("dashboard"))
    return render_template("/pages/admin/add_post.html", title=title)


@app.route("/dashboard")
@login_required
def dashboard():
    title = "Admin Dashboard"
    posts = load_posts()
    return render_template("pages/admin/dashboard.html", title=title, posts=posts)
