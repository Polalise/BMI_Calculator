from routes.bmi_routes import bmi_bp, init_db as init_bmi_db
from routes.history_routes import history_bp, init_db as init_history_db
from routes.member_routes import member_bp
from routes.statistics_routes import statistics_bp, init_db as init_statistics_db


def register_routes(app, db):
    """애플리케이션에 모든 Blueprint를 등록합니다."""
    init_bmi_db(db)
    init_history_db(db)
    init_statistics_db(db)

    app.register_blueprint(bmi_bp)
    app.register_blueprint(history_bp)
    app.register_blueprint(member_bp)
    app.register_blueprint(statistics_bp)
