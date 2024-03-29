from flask import request, render_template
from flask_jwt_extended import create_access_token, decode_token
from app.database.models import User
from flask_restful import Resource
import datetime
from app.resources.errors import (
    SchemaValidationError,
    InternalServerError,
    EmailDoesnotExistsError,
    BadTokenError,
)
from jwt.exceptions import ExpiredSignatureError, DecodeError, InvalidTokenError

from app.services.mail_service import send_email, sendflask_email


class ForgotPassword(Resource):
    def post(self):
        url = request.host_url + "reset/"
        try:
            body = request.get_json()
            email = body.get("email")
            if not email:
                raise SchemaValidationError

            # user = User.objects.get(email=email)
            # if not user:
            #     raise EmailDoesnotExistsError

            # expires = datetime.timedelta(hours=24)
            # reset_token = create_access_token(str(user.id), expires_delta=expires)

            send_email.delay(
                "Reset Your Password",
                recipients=[email],
                text_body=render_template(
                    "email/reset_password.txt", url=url + "reset_token"
                ),
                html_body=render_template(
                    "email/reset_password.html", url=url + "reset_token"
                ),
            )
            return {"Password reset url": url + "reset_token"}, 200
        except SchemaValidationError:
            raise SchemaValidationError
        except EmailDoesnotExistsError:
            raise EmailDoesnotExistsError
        except Exception as e:
            raise InternalServerError


class ResetPassword(Resource):
    def post(self):
        url = request.host_url + "reset/"
        try:
            body = request.get_json()
            reset_token = body.get("reset_token")
            password = body.get("password")

            if not reset_token or not password:
                raise SchemaValidationError

            user_id = decode_token(reset_token)["identity"]

            user = User.objects.get(id=user_id)

            user.modify(password=password)
            user.hash_password()
            user.save()
            send_email.delay(
                "Password reset successful",
                sender="support@test-bag.com",
                recipients=[user.email],
                text_body="Password reset was successful",
                html_body="<p>Password reset was successful</p>",
            )

            return {"Password reset was successful for": user.email}, 200

        except SchemaValidationError:
            raise SchemaValidationError
        except ExpiredSignatureError:
            raise BadTokenError
        except (DecodeError, InvalidTokenError):
            raise BadTokenError
        except Exception as e:
            raise InternalServerError
