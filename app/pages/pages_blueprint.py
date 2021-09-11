import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from wtforms.validators import (DataRequired, Email,EqualTo,Length,URL)
from wtforms import Form, BooleanField, StringField, PasswordField, validators
import os
from datetime import datetime
import json
import string
from app import mongo
from flask import jsonify
from flask import session

from flask import (
    Blueprint, render_template, redirect,
    request, url_for, flash, session, Markup)
from werkzeug.security import check_password_hash, generate_password_hash


pages_blueprint = Blueprint("pages_blueprint", __name__,
    template_folder ='templates',
    static_folder ='static', 
    static_url_path='/assets'

)

@pages_blueprint.route('/')
def index():
    return render_template('index.html')

# ----------------- Routes to Pages ------------------ #


@pages_blueprint.route('/getting_started')
def getting_started():
    return render_template('getting_started.html')




@pages_blueprint.route('/about')
def about():
    return render_template('about.html')

@pages_blueprint.route('/info')
def info():
    return render_template('info.html')

@pages_blueprint.route('/mission')
def mission():
    return render_template('mission.html')

@pages_blueprint.route('/team')
def team():
    return render_template('team.html')



@pages_blueprint.route('/profile')
def profile():
    channel_Name= mongo.db.channel.find()
    users = mongo.db.users.find()
    messages_All = mongo.db.message.find()
    
    return render_template('profile.html',  users=users, channel_Name=channel_Name, messages_All=messages_All)

