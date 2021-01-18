from flask_pymongo import PyMongo
from flask import Flask, render_template, redirect, request, url_for, session, flash
from app.config import Config, DevelopmentConfig
import os
import config 


mongo = PyMongo()

def create_app(config):
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    app.config.from_object('app.config.DevelopmentConfig')
    mongo.init_app(app)
    return app
