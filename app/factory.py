from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

# from flask_mail import Mail
from app.database.db import initialize_db
from flask_restful import Api
from app.resources.errors import errors


def create_app():
    app = Flask(__name__)
    app.config.from_envvar("ENV_FILE_LOCATION")
    api = Api(app, errors=errors)
    # imports requiring app and mail
    from app.resources.routes import initialize_routes

    bcrypt = Bcrypt(app)
    jwt = JWTManager(app)

    initialize_db(app)
    initialize_routes(api)

    return app

