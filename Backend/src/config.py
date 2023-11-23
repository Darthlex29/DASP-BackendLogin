import os
import secrets

class Config:
    SECRET_KEY = 'SECRET_KEY'
    
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://udwocckwfv06wzu9:B4rSteiAKzbEvLL3Laui@brs91absj0pvf3xov5we-mysql.services.clever-cloud.com/brs91absj0pvf3xov5we'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False

finalConfig = {
    "development": DevelopmentConfig,
    'production': ProductionConfig
}