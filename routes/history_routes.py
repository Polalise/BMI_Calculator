from flask import Blueprint, render_template

history_bp = Blueprint("history", __name__)

db = None

def init_db(database_instance):
    global db
    db = database_instance


@history_bp.route("/history")
def history():
    records = db.get_bmi_records(10)
    return render_template("history.html", records=records)