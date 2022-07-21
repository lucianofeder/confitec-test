from flask import Flask
from resources import routes


def create_app() -> Flask:
    app = Flask(__name__)
    routes.init_app(app)
    return app
