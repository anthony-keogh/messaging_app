import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import os
from datetime import datetime
import json
import string
from flask import jsonify
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash
from app.pages.pages_blueprint import pages_blueprint
from app.users.users_blueprint import users_blueprint
from app.messages.messages_blueprint import messages_blueprint
from app.channels.channels_blueprint import channels_blueprint
from app.config import Config
from flask import Blueprint
from app import create_app, mongo


app = create_app(Config)


if os.path.isfile('env.py'):
    import env

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.register_blueprint(users_blueprint)
app.register_blueprint(pages_blueprint)
app.register_blueprint(messages_blueprint)
app.register_blueprint(channels_blueprint)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=False)