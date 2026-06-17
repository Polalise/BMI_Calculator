from flask import Blueprint, render_template, request

from services.bmi_service import BMICalculator


bmi_bp = Blueprint("bmi", __name__)

db = None


def init_db(database_instance):
    """BMI 라우트에서 사용할 DB 인스턴스를 설정합니다."""
    global db
    db = database_instance


@bmi_bp.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@bmi_bp.route("/calculate", methods=["POST"])
def calculate():
    try:
        weight = float(request.form["weight"])
        height = float(request.form["height"])

        if weight <= 0 or height <= 0:
            return render_template("index.html", error="체중과 신장은 양수여야 합니다.")

        calculator = BMICalculator(weight, height)
        result = calculator.get_result()

        db.save_bmi_record(weight, height, result["bmi"], result["category"])

        return render_template(
            "result.html",
            bmi=result["bmi"],
            category=result["category"],
            weight=weight,
            height=height,
        )
    except ValueError:
        return render_template("index.html", error="유효한 숫자를 입력해주세요.")
