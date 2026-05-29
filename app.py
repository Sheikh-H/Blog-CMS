from flask import render_template, redirect, url_for, Flask, session, request
import werkzeug
import sys
import os
from datetime import datetime
from helpers.auth import login_required, login_function
import secrets
from dotenv import load_dotenv
from flask_session import Session

load_dotenv()


app = Flask(__name__)

app.secret_key = os.environ.get("SECRET_KEY")


@app.route("/")
def home():
    title = "Roadmap.sh Blog"
    return render_template("pages/home.html", title=title)


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


@app.route("/dashboard")
@login_required
def dashboard():
    title = "Admin Dashboard"
    return render_template("pages/admin/dashboard.html", title=title)
