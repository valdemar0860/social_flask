from flask import Blueprint, render_template
user_pages = Blueprint("user_pages", __name__)
@user_pages.route("/register")
def register():
    return render_template("users/register.html")