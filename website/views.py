# store routes in website

from flask import Blueprint, render_template

# set a blueprint for the application
views = Blueprint("views", __name__)


# set a route to homepage
@views.route("/")
def home():
    return render_template("home.html")
