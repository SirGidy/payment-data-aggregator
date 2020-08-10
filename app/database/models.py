from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash


class Customer(db.Document):
    bvn = db.IntField(required=True, unique=True)
    email = db.EmailField(required=True, unique=True)
    phone_number = db.StringField(required=True, unique=True)
    last_name = db.StringField(required=True)
    first_name = db.StringField(required=True)
    middle_name = db.StringField()
    mygender = ("FEMALE", "MALE")
    gender = db.StringField(choices=mygender)
    marital_status = ("MARRIED", "SINGLE", "DIVORCED")
    marital_status = db.StringField(choices=marital_status)
    state_of_origin = db.StringField()
    address = db.StringField()
    state = db.StringField()
    post_code = db.StringField()
    city = db.StringField()
    country = db.StringField()
    # added_by = db.ReferenceField('User')


class Merchant(db.Document):
    name = db.StringField(required=True, unique=True)
    phone_number = db.StringField(required=True, unique=True)
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode("utf8")

    def check_password(self, password):
        return check_password_hash(self.password, password)


class User(db.Document):
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)
    # movies = db.ListField(db.ReferenceField('Movie', reverse_delete_rule=db.PULL))

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode("utf8")

    def check_password(self, password):
        return check_password_hash(self.password, password)

