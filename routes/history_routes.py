from flask import Blueprint, render_template, session

history_bp = Blueprint("history", __name__)

db = None


def init_db(database_instance):
    global db
    db = database_instance


@history_bp.route("/history")
def history():
    login_id = session.get("login_id")

    if login_id is None:
        return render_template("history.html", records=[])

    records = db.get_bmi_records(login_id, 10)
    return render_template("history.html", records=records)
