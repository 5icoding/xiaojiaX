from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

from .zoo import api

from .extensions import db


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:123456@localhost:3306/sites'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    app.wsgi_app = ProxyFix(app.wsgi_app)

    api.init_app(app)

    return app