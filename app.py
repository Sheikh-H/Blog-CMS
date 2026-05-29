from flask import render_template, redirect, url_for, Flask, session, request
import werkzeug
import sys
import os
from datetime import datetime
from helpers.auth import login_required, login_function
import secrets
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)

app.secret_key = os.environ.get("SECRET_KEY")


@app.route("/")
def home():
    title = "Roadmap.sh Blog"
    return render_template("pages/home.html", title=title)


@app.route("/admin", methods=["GET", "POST"])
def admin():
    title = "Admin Login"
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        login = login_function(username, password)
        if login == True:
            session["admin_id"] = 1
            return redirect(url_for("dashboard"))
        else:
            return redirect(url_for("admin"))

    return render_template("pages/admin/admin.html", title=title)


@app.route("/dashboard")
@login_required
def dashboard():
    title = "Admin Dashboard"
    return render_template("pages/admin/dashboard.html", title=title)
