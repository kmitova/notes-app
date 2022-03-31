# store routes in website

from flask import Blueprint

# set a blueprint for the application
views = Blueprint("views", __name__)

# set a route to homepage
@views.route("/")
def home():
    return "<h1>Test</h1>"
