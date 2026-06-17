import atexit

from flask import Flask, request, session

from config import dbSetting
from models import Database
from routes import register_routes


def get_action_type(method):
    action_map = {
        "GET": "SELECT",
        "POST": "INSERT",
        "PUT": "UPDATE",
        "PATCH": "UPDATE",
        "DELETE": "DELETE",
    }
    return action_map.get(method, "REQUEST")


def should_log_request():
    if request.endpoint == "static":
        return False

    excluded_paths = (
        "/static/",
        "/favicon.ico",
    )
    return not request.path.startswith(excluded_paths)


def create_app():
    """Flask 애플리케이션을 생성하고 설정합니다."""
    app = Flask(__name__)
    app.config.from_object(dbSetting)

    db = Database()
    atexit.register(db.close)

    register_routes(app, db)

    @app.after_request
    def save_request_log(response):
        if should_log_request():
            db.save_activity_log(
                action_type=get_action_type(request.method),
                description=f"{request.method} {request.path}",
                member_id=session.get("member_id"),
                request_uri=request.path,
                http_method=request.method,
                status_code=response.status_code,
            )

        return response

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
