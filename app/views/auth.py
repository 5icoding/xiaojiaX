import functools

from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

from app.extensions import db
from app.models import User

auth = Blueprint("auth", __name__, url_prefix="/auth")

def login_required(view):
    """View decorator that redirects anonymous users to the login page."""
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("auth.login"))
        return view(**kwargs)
    return wrapped_view


@auth.before_app_request
def load_logged_in_user():
    """If a user id is stored in the session, load the user object from
    the database into ``g.user``."""
    user_id = session.get("user_id")

    if user_id is None:
        g.user = None
    else:
        # with SQLHelper() as helper:
        #     user_list = helper.fetchone('select * from users WHERE id = ?', (user_id))
        user = User.query.filter(User.id == user_id).first()
        g.user = user
        print(g.user.role)

@auth.route("/login", methods=("GET", "POST"))
def login():
    """Log in a registered user by adding the user id to the session."""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        print(username, password)
        error = None

        user = User.query.filter(User.username == username).first()
        print(user)

        if user is None:
            error = "Incorrect username."
        elif not (user.password == password):
            error = "Incorrect password."

        if error is None:
            # store the user id in a new session and return to the index
            session.clear()
            session["user_id"] = user.id
            print("session['user_id']->"+str(session["user_id"]))
            session["user_name"] = user.username
            session["user_role"] = user.role
            
            if user.role == 1:
                return redirect(url_for("study.index"))
            if user.role == 10:
                return redirect(url_for("design.index"))
            return redirect(url_for("site.index"))

        flash(error)

    return render_template("auth/login.html")


@auth.route("/logout")
def logout():
    """Clear the current session, including the stored user id."""
    session.clear()
    return redirect(url_for("site.index"))
