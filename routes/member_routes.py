from flask import Blueprint, redirect, render_template, request, session, url_for

from services.member_service import login_member, signup_member


member_bp = Blueprint("member", __name__, url_prefix="/member")

db = None


def init_db(database_instance):
    global db
    db = database_instance


@member_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        result = login_member(
            db,
            login_id=request.form.get("login_id"),
            password=request.form.get("password"),
        )

        if result["success"]:
            member = result["member"]
            session["login_id"] = member["login_id"]
            session["name"] = member["name"]
            return redirect(url_for("bmi.bmi_form"))

        return render_template("login.html", error=result["message"])

    return render_template("login.html")


@member_bp.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        result = signup_member(
            db,
            login_id=request.form.get("login_id"),
            password=request.form.get("password"),
            name=request.form.get("name"),
        )

        if result["success"]:
            return redirect(url_for("member.login"))

        return render_template("signup.html", error=result["message"])

    return render_template("signup.html")
