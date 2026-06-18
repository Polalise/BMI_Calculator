from flask import Blueprint, redirect, render_template, session, url_for

from services.history_service import HistoryService

history_bp = Blueprint("history", __name__)

history_service = None



def init_db(database_instance):
    global history_service
    history_service = HistoryService(database_instance)


@history_bp.route("/history")
def history():
    member_id = session.get("member_id")

    if member_id is None:
        return render_template("history.html", records=[])

    records = history_service.get_recent_records(member_id, 10)
    return render_template("history.html", records=records)


@history_bp.route("/history/delete/<int:record_id>", methods=["POST"])
def delete_history(record_id):
    member_id = session.get("member_id")

    if member_id is None:
        return redirect(url_for("member.login"))

    history_service.delete_record(record_id, member_id)
    return redirect(url_for("history.history"))
