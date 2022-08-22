
from flask import Flask
from lib import db,cache

class BaseConfig:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./data.db'
    SQLALCHEMY_ECHO = True

def create_app():
    app = Flask(__name__)
    app.config.from_object(BaseConfig)
    cache.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
        db.session.commit()
    return app


