from flask import Flask

from app.db import db
from app.file_uploader import file_upload_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.ProdConfig')
    app.register_blueprint(file_upload_bp)
    db.init_app(app)
    db.app = app
    db.create_all()
    return app



