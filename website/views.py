# store routes in website

from flask import Blueprint, render_template
from flask_login import login_required, current_user

# set a blueprint for the application
views = Blueprint("views", __name__)


# set a route to homepage
@views.route("/")
@login_required
def home():
    return render_template("home.html", user=current_user)
