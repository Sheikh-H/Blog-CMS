from flask import render_template, redirect, url_for, Flask, session, request
import wtforms
import werkzeug
import sys
import os
from datetime import datetime
from helpers.auth import login_required

app = Flask(__name__)


@app.route("/")
def home():
    title = "Roadmap.sh Blog"
    return render_template("pages/home.html", title=title)


@app.route("/admin", methods=["GET", "POST"])
def admin():
    title = "Admin Login"
    if request.method == "POST":
        session["admin_id"] = 1
    return render_template("admin.html", title=title)


@app.route("/dashboard")
@login_required
def dashboard():
    title = "Admin Dashboard"
