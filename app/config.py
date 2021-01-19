import os
from flask import Flask
import config
from app import create_app

app = Flask(__name__)

class Config(object):
    DEBUG = False
    TESTING = False
    MONGO_DBNAME = app.config["MONGO_DBNAME"] = os.environ.get('MONGO_DBNAME')
    MONGO_URI = app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
    SECRET_KEY = os.getenv("SECRET_KEY")
    
    DATABASE_URI = os.environ.get('MONGO_URI')
class ProductionConfig(Config):
    DEBUG = False
    

class DevelopmentConfig(Config):
    DEBUG = True
    MONGO_DBNAME = app.config["MONGO_DBNAME"] = os.environ.get('MONGO_DBNAME')
    MONGO_URI = app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
    SECRET_KEY = os.getenv("SECRET_KEY")
    
    DATABASE_URI = os.environ.get('MONGO_URI')
    TESTING = True
   
    #app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

class TestingConfig(Config):
    TESTING = True