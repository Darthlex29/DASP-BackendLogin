from decouple import config
import os
import secrets

class Config:
    SECRET_KEY = config('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = config('SQLALCHEMY_DATABASE_URI') or \
        'mysql://root:root@localhost/new_schema'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
config = {
    "development": DevelopmentConfig,
    'production': ProductionConfig
}