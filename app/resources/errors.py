class InternalServerError(Exception):
    pass


class SchemaValidationError(Exception):
    pass


class MovieAlreadyExistsError(Exception):
    pass


class UpdatingMovieError(Exception):
    pass


class DeletingMovieError(Exception):
    pass


class MovieNotExistsError(Exception):
    pass


class CustomerAlreadyExistsError(Exception):
    pass


class UpdatingCustomerError(Exception):
    pass


class DeletingCustomerError(Exception):
    pass


class CustomerNotExistsError(Exception):
    pass


class MerchantAlreadyExistsError(Exception):
    pass


class UpdatingMerchantError(Exception):
    pass


class DeletingMerchantError(Exception):
    pass


class MerchantNotExistsError(Exception):
    pass


class EmailAlreadyExistsError(Exception):
    pass


class UnauthorizedError(Exception):
    pass


class EmailDoesnotExistsError(Exception):
    pass


class BadTokenError(Exception):
    pass


errors = {
    "InternalServerError": {"message": "Something went wrong", "status": 500},
    "SchemaValidationError": {
        "message": "Request is missing required fields",
        "status": 400,
    },
    "MovieAlreadyExistsError": {
        "message": "Movie with given name already exists",
        "status": 400,
    },
    "UpdatingMovieError": {
        "message": "Updating movie added by other is forbidden",
        "status": 403,
    },
    "DeletingMovieError": {
        "message": "Deleting movie added by other is forbidden",
        "status": 403,
    },
    "MovieNotExistsError": {
        "message": "Movie with given id doesn't exists",
        "status": 400,
    },
    "CustomerAlreadyExistsError": {"message": "Customer already exists", "status": 400},
    "UpdatingCustomerError": {
        "message": "Updating customer added by other is forbidden",
        "status": 403,
    },
    "DeletingCustomerError": {
        "message": "Deleting customer added by other is forbidden",
        "status": 403,
    },
    "CustomerNotExistsError": {
        "message": "Customer with given id doesn't exists",
        "status": 400,
    },
    "MerchantAlreadyExistsError": {
        "message": "Merchant with given name already exists",
        "status": 400,
    },
    "UpdatingMerchantError": {
        "message": "Updating merchant added by other is forbidden",
        "status": 403,
    },
    "DeletingMechantError": {
        "message": "Deleting merchant added by other is forbidden",
        "status": 403,
    },
    "MerchantNotExistsError": {
        "message": "Merchant with given id doesn't exists",
        "status": 400,
    },
    "EmailAlreadyExistsError": {
        "message": "User with given email address already exists",
        "status": 400,
    },
    "UnauthorizedError": {"message": "Invalid username or password", "status": 401},
    "EmailDoesnotExistsError": {
        "message": "Couldn't find the user with given email address",
        "status": 400,
    },
    "BadTokenError": {"message": "Invalid token", "status": 403},
}
