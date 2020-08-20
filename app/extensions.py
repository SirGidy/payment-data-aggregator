from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

# from celery import Celery

from flask_mail import Mail
from app.database.db import initialize_db


from flask_restful import Api
from app.resources.errors import errors
from app.celery_utils import init_celery

from app.services.mailer import initialize_mail

# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import Mail


bcrypt = Bcrypt()
jwt = JWTManager()
