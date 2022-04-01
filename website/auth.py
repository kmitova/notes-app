from flask import Blueprint, render_template

# set a blueprint for the application
auth = Blueprint("auth", __name__)


@auth.route("/login")
def login():
    return render_template("login.html", boolean=False)


@auth.route("/logout")
def logout():
    return "<p>Logout</p>"


@auth.route("/sign-up")
def sign_up():
    return render_template("signup.html")
