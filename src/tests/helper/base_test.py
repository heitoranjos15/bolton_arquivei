import os
import random
from flask_testing import TestCase

from app import create_app
from config import configs

db = configs.get('test').db


class BaseTestCase(TestCase):

    def create_app(self):
        os.environ['service_env'] = 'test'
        app = create_app()
        return app

    def setUp(self):
        self.create_app()
        from src.models.invoice import Invoice
        self.mocks_db(Invoice)

    def tearDowm(self):
        db.session.remove()
        db.drop_all()

    def mocks_db(self, invoice):
        mock = invoice(access_key='123', value='xml')
        db.session.add(mock)
        db.session.commit()
