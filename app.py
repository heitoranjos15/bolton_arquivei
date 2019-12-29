import os

from flask import Flask
from sqlalchemy import create_engine
from flask_restful import Api
from flask_migrate import Migrate


from src.routes import add_routes
from config import configs


def create_app():
    env = configs.get(os.environ.get('service_env', 'dev'))
    db = env.db
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = env.db_host
    app.engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    api = Api(app)
    add_routes(api)

    from src.models.invoice import Invoice
    db.app = app
    db.init_app(app)
    Migrate(app, db)

    return app
