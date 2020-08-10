from flask import Response, request
from app.database.models import Customer, User
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from mongoengine.errors import (
    FieldDoesNotExist,
    NotUniqueError,
    DoesNotExist,
    ValidationError,
    InvalidQueryError,
)
from app.resources.errors import (
    SchemaValidationError,
    CustomerAlreadyExistsError,
    InternalServerError,
    UpdatingCustomerError,
    DeletingCustomerError,
    CustomerNotExistsError,
)


class CustomersApi(Resource):
    @jwt_required
    def get(self):
        customers = Customer.objects().to_json()
        return Response(customers, mimetype="application/json", status=200)

    @jwt_required
    def post(self):
        try:
            user_id = get_jwt_identity()
            body = request.get_json()
            # user = User.objects.get(id=user_id)
            # customer =  Customer(**body,added_by=user)
            customer = Customer(**body)
            customer.save()
            # user.update(push__customers=customer)
            # user.save()
            id = customer.id
            return {"id": str(id)}, 200
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise CustomerAlreadyExistsError
        except Exception as e:
            raise


class CustomerApi(Resource):
    @jwt_required
    def put(self, id):
        try:
            user_id = get_jwt_identity()
            customer = Customer.objects.get(id=id)
            body = request.get_json()
            Customer.objects.get(id=id).update(**body)
            return "", 200
        except InvalidQueryError:
            raise SchemaValidationError
        except DoesNotExist:
            raise UpdatingCustomerError
        except Exception:
            raise InternalServerError

    @jwt_required
    def delete(self, id):
        try:
            user_id = get_jwt_identity()
            customer = Customer.objects.get(id=id)
            customer.delete()
            return "", 200
        except DoesNotExist:
            raise DeletingCustomerError
        except Exception:
            raise InternalServerError

    @jwt_required
    def get(self, id):
        try:
            customer = Customer.objects.get(id=id).to_json()
            return Response(customer, mimetype="application/json", status=200)
        except DoesNotExist:
            raise CustomerNotExistsError
        except Exception:
            raise InternalServerError


class CustomerByBVNApi(Resource):
    @jwt_required
    def get(self, id):
        try:
            customer = Customer.objects.get(bvn=id).to_json()
            return Response(customer, mimetype="application/json", status=200)
        except DoesNotExist:
            raise CustomerNotExistsError
        except Exception:
            raise InternalServerError


class CustomerByPhoneNumberApi(Resource):
    @jwt_required
    def get(self, id):
        try:
            customer = Customer.objects.get(phone_number=id).to_json()
            return Response(customer, mimetype="application/json", status=200)
        except DoesNotExist:
            raise CustomerNotExistsError
        except Exception:
            raise InternalServerError


class CustomerByEmailApi(Resource):
    @jwt_required
    def get(self, id):
        try:
            customer = Customer.objects.get(email=id).to_json()
            return Response(customer, mimetype="application/json", status=200)
        except DoesNotExist:
            raise CustomerNotExistsError
        except Exception:
            raise InternalServerError
