from flask import Blueprint, redirect, render_template, request, session, url_for

from services.bmi_service import BMICalculator


bmi_bp = Blueprint("bmi", __name__)

db = None


def init_db(database_instance):
    global db
    db = database_instance


@bmi_bp.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@bmi_bp.route("/bmi", methods=["GET"])
def bmi_form():
    is_logged_in = session.get("member_id") is not None
    return render_template("bmi.html", is_logged_in=is_logged_in)


@bmi_bp.route("/calculate", methods=["POST"])
def calculate():
    member_id = session.get("member_id")

    if member_id is None:
        return redirect(url_for("member.login"))

    try:
        weight = float(request.form["weight"])
        height = float(request.form["height"])

        if weight <= 0 or height <= 0:
            return render_template(
                "bmi.html",
                error="Weight and height must be greater than 0.",
                is_logged_in=True,
            )

        calculator = BMICalculator(weight, height)
        result = calculator.get_result()

        db.save_bmi_record(
            weight,
            height,
            result["bmi"],
            result["category"],
            member_id=member_id,
        )

        return render_template(
            "result.html",
            bmi=result["bmi"],
            category=result["category"],
            weight=weight,
            height=height,
        )
    except ValueError:
        return render_template(
            "bmi.html",
            error="Please enter valid numbers.",
            is_logged_in=True,
        )
