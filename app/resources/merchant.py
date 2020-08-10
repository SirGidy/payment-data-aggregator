from flask import Response, request
from flask_jwt_extended import create_access_token
from app.database.models import Merchant
from flask_restful import Resource
import datetime
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist
from app.resources.errors import (
    SchemaValidationError,
    EmailAlreadyExistsError,
    UnauthorizedError,
    InternalServerError,
)


class MerchantApi(Resource):
    def post(self):
        try:
            body = request.get_json()
            merchant = Merchant(**body)
            merchant.hash_password()
            merchant.save()
            id = merchant.id
            return {"id": str(id)}, 200
        except FieldDoesNotExist:
            raise SchemaValidationError
        except NotUniqueError:
            raise EmailAlreadyExistsError
        except Exception as e:
            raise InternalServerError


class MerchantTokenApi(Resource):
    def post(self):
        try:
            body = request.get_json()
            user = Merchant.objects.get(email=body.get("email"))
            authorized = user.check_password(body.get("password"))
            if not authorized:
                return {"error": "Email or password invalid"}, 401

            expires = datetime.timedelta(days=360)
            access_token = create_access_token(
                identity=str(user.id), expires_delta=expires
            )
            return {"token": access_token}, 200
        except (UnauthorizedError, DoesNotExist):
            raise UnauthorizedError
        except Exception as e:
            raise InternalServerError
