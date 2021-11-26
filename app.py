from flask import Flask

from settings import schedule_config, config
from models import db
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    app.config.from_object(schedule_config)
    db.init_app(app)

    # 解决跨域问题
    CORS(app)
    return app
