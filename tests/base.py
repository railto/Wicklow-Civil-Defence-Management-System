from flask_testing import TestCase

from app import create_app, db
from config import Config


class TestConfig(Config):
    FLASK_ENV = 'testing'
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/wicklowcd_test'
    BCRYPT_LOG_ROUNDS = 4
    SECRET_KEY = 'NotSoSecret'


class BaseTestCase(TestCase):
    def create_app(self):
        app = create_app()
        app.config.from_object(TestConfig)
        return app

    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
