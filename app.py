from flask import render_template, redirect, url_for, Flask
import wtforms
import werkzeug
import sys
import os
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    title = "Roadmap.sh Blog"
    return render_template("pages/home.html", title=title)
