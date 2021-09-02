from posix import environ
from flask import Flask
import os
from src.database import db
from src.api import auth
from flask_jwt_extended import JWTManager


def create_app(test_config=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY=os.environ.get("SECRET_KEY"),
            SQLALCHEMY_DATABASE_URI=os.environ.get("DB_URL"),
            JWT_SECRET_KEY=os.environ.get("JWT_SECRET_KEY")
        )
    else:
        app.config.from_mapping(test_config)

    db.app = app
    db.init_app(app)
    app.register_blueprint(auth)
    jwt = JWTManager(app)

    with app.app_context():
        db.create_all()
    return app


app = create_app()
