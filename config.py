import os

ENV = os.environ.get('ENV', 'DEV')


class BaseConfig():
    TESTING = True
    DEBUG = ENV == 'DEV'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


class ProdConfig(BaseConfig):
    TESTING = False
    DEBUG = False
