from functools import wraps
from flask import session, redirect, url_for
from pathlib import Path
from werkzeug.security import generate_password_hash, check_password_hash
import json
import os

base_dir = Path(__file__).resolve().parent.parent
admin_path = base_dir / "instance" / "admin.json"


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "admin_id" not in session:
            return redirect(url_for("admin"))
        return f(*args, **kwargs)

    return decorated_function


def login_function(username, password):
    if not os.path.exists(admin_path):
        return "Please create login details first", 400
    else:
        with open(admin_path, "r") as f:
            user = json.load(f)
        if not user[0]["username"] == username:
            return False
        try:
            check_password_hash(user[0]["password"], password)
            return True
        except:
            return False


def register_user(username, password):
    user = {"username": username, "password": generate_password_hash(password)}
    if not os.path.exists(admin_path):
        with open(admin_path, "w") as f:
            json.dump([], f)
        with open(admin_path, "r") as f:
            data = json.load(f)
            data.append(user)
        with open(admin_path, "w") as f:
            json.dump(data, f, indent=2)
    else:
        with open(admin_path, 'r') as f:
            data = json.load(f)
        with open(admin_path, "w") as f:
            data.append(user)
            json.dump(data, f, indent=2)


# To register a user please use the following function and run python file in terminal:
register_user("admin", "password123")
