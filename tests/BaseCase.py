import unittest

from app import app
from database.db import db


class BaseCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.db = db.get_db()


    def tearDown(self):
        pass
      
