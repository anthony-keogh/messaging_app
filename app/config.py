import os
from flask import Flask
import config


class Config(object):
    DEBUG = False
    TESTING = False
    MONGO_DBNAME = 'CookbookFask'
    MONGO_URI = os.environ.setdefault("MONGO_URI", 'mongodb://AnthonyKeogh:45hungryhill@cookbookfask-shard-00-00-t3cez.mongodb.net:27017,cookbookfask-shard-00-01-t3cez.mongodb.net:27017,cookbookfask-shard-00-02-t3cez.mongodb.net:27017/test?ssl=true&replicaSet=CookbookFask-shard-0&authSource=admin&retryWrites=true&w=majority')
    SECRET_KEY = os.getenv("SECRET_KEY")
    
    DATABASE_URI = os.environ.setdefault("MONGO_URI", 'mongodb://AnthonyKeogh:45hungryhill@cookbookfask-shard-00-00-t3cez.mongodb.net:27017,cookbookfask-shard-00-01-t3cez.mongodb.net:27017,cookbookfask-shard-00-02-t3cez.mongodb.net:27017/test?ssl=true&replicaSet=CookbookFask-shard-0&authSource=admin&retryWrites=true&w=majority')

class ProductionConfig(Config):
    DEBUG = False
    

class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_URI = os.environ.setdefault("MONGO_URI", 'mongodb://AnthonyKeogh:45hungryhill@cookbookfask-shard-00-00-t3cez.mongodb.net:27017,cookbookfask-shard-00-01-t3cez.mongodb.net:27017,cookbookfask-shard-00-02-t3cez.mongodb.net:27017/test?ssl=true&replicaSet=CookbookFask-shard-0&authSource=admin&retryWrites=true&w=majority')
    TESTING = True
    MONGO_DBNAME = 'CookbookFask'
    MONGO_URI = os.environ.setdefault("MONGO_URI", 'mongodb://AnthonyKeogh:45hungryhill@cookbookfask-shard-00-00-t3cez.mongodb.net:27017,cookbookfask-shard-00-01-t3cez.mongodb.net:27017,cookbookfask-shard-00-02-t3cez.mongodb.net:27017/test?ssl=true&replicaSet=CookbookFask-shard-0&authSource=admin&retryWrites=true&w=majority')
    SECRET_KEY = os.getenv("SECRET_KEY")
    #app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

class TestingConfig(Config):
    TESTING = True