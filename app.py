import atexit

from flask import Flask

from config import dbSetting
from models import Database
from routes import register_routes


def create_app():
    """Flask 애플리케이션을 생성하고 설정합니다."""
    app = Flask(__name__)
    app.config.from_object(dbSetting)

    db = Database()
    atexit.register(db.close)

    register_routes(app, db)

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
