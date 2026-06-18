from flask import Blueprint, render_template

from services.statistics_service import StatisticsService


statistics_bp = Blueprint("statistics", __name__, url_prefix="/statistics")

db = None


def init_db(database_instance):
    global db
    db = database_instance


@statistics_bp.route("/", methods=["GET"])
def statistics():
    service = StatisticsService(db)
    data = service.get_statistics()
    return render_template("statistics.html", statistics=data)
