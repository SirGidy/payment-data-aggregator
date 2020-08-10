from .customer import (
    CustomersApi,
    CustomerApi,
    CustomerByBVNApi,
    CustomerByEmailApi,
    CustomerByPhoneNumberApi,
)
from .merchant import MerchantApi, MerchantTokenApi
from .auth import SignupApi, LoginApi
from .reset_password import ForgotPassword, ResetPassword


def initialize_routes(api):
    api.add_resource(CustomersApi, "/api/customers")
    api.add_resource(CustomerApi, "/api/customer/<id>")

    api.add_resource(CustomerByBVNApi, "/api/customer/bvn/<id>")
    api.add_resource(CustomerByPhoneNumberApi, "/api/customer/phonenumber/<id>")
    api.add_resource(CustomerByEmailApi, "/api/customer/email/<id>")

    api.add_resource(MerchantApi, "/api/merchant/signup")
    api.add_resource(MerchantTokenApi, "/api/merchant/token")

