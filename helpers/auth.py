from functools import wraps
from flask import session, redirect, url_for
import werkzeug


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "admin_id" not in session:
            return redirect(url_for("admin"))
        return f(*args, **kwargs)

    return decorated_function


def login_function(username, password):
    if username == "sheikh_hussain" and password == "Password123":
        return True
    else:
        return False
