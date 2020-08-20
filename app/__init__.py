from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from celery import Celery
from flask_mail import Mail
from app.database.db import initialize_db
from flask_restful import Api
from app.resources.errors import errors
from app.celery_utils import init_celery
from sendgrid import SendGridAPIClient
from celery.schedules import crontab

# from celery.decorators import periodic_task
# Globally accessible libraries
celery = Celery(__name__)
bcrypt = Bcrypt()
jwt = JWTManager()


def create_app(**kwargs):
    app = Flask(__name__)
    app.config.from_envvar("ENV_FILE_LOCATION")

    # Initialize Plugins
    jwt.init_app(app)
    bcrypt.init_app(app)
    api = Api(app, errors=errors)
    initialize_db(app)

    with app.app_context():
        if kwargs.get("celery"):
            init_celery(kwargs.get("celery"), app)

        # imports requiring app and mail
        from app.resources.routes import initialize_routes

        initialize_routes(api)
        return app


def make_celery(app_name=__name__):
    return Celery(app_name)
