import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG=False
    TESTING=False
    CSRF_ENABLED=True
    SECRET_KEY='12345678'

class ProductionConfig(Config):
    DEBUG=False

class StagingConfig(Config):
    DEVELOPMENT=True
    DEBUG=True

class DevelopmentConfig(Config):
    DEVELOPMENT=True
    DEBUG=True

class TestingConfig(Config):
    TESTING=True
