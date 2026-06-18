from flask import Blueprint, redirect, render_template, url_for

from services.history_service import HistoryService

history_bp = Blueprint("history", __name__)

history_service = None



def init_db(database_instance):
    global history_service
    history_service = HistoryService(database_instance)


@history_bp.route("/history")
def history():
    login_id = session.get("login_id")

    if login_id is None:
        return render_template("history.html", records=[])

    records = history_service.get_recent_records(10)
    return render_template("history.html", records=records)


@history_bp.route("/history/delete/<int:record_id>", methods=["POST"])
def delete_history(record_id):
    history_service.delete_record(record_id)
    return redirect(url_for("history.history"))