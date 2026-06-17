from flask import Blueprint, redirect, render_template, request, session, url_for

from services.member_service import MemberService


member_bp = Blueprint("member", __name__, url_prefix="/member")

member_service = None


def init_db(database_instance):
    global member_service
    member_service = MemberService(database_instance)


@member_bp.route("/login", methods=["GET"])
def login():
    return render_template("login.html")


@member_bp.route("/login", methods=["POST"])
def login_submit():
    login_id = request.form["login_id"]
    password = request.form["password"]

    success, message, member = member_service.login(login_id, password)

    if not success:
        return render_template("login.html", error=message)

    session["member_id"] = member["id"]
    session["user_id"] = member["user_id"]
    session["name"] = member["name"]

    return redirect(url_for("bmi.bmi_form"))


@member_bp.route("/signup", methods=["GET"])
def signup():
    return render_template("signup.html")


@member_bp.route("/signup", methods=["POST"])
def signup_submit():
    login_id = request.form["login_id"]
    password = request.form["password"]
    name = request.form["name"]

    success, message, member = member_service.signup(login_id, password, name)

    if not success:
        return render_template("signup.html", error=message)

    session["member_id"] = member["id"]
    session["user_id"] = member["user_id"]
    session["name"] = member["name"]

    return redirect(url_for("bmi.bmi_form"))


@member_bp.route("/logout", methods=["GET"])
def logout():
    session.clear()
    return redirect(url_for("bmi.index"))
