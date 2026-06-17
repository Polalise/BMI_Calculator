from flask import Blueprint, render_template


member_bp = Blueprint("member", __name__, url_prefix="/member")


@member_bp.route("/login", methods=["GET"])
def login():
    return render_template("login.html")


@member_bp.route("/signup", methods=["GET"])
def signup():
    return render_template("signup.html")
