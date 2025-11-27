from flask import render_template
from models import users

def home_controller():
    return render_template("index.html")

def users_controller():
    return render_template("users.html", users=users)
