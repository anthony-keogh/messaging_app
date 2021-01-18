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


users_blueprint = Blueprint("users_blueprint", __name__,
    template_folder ='templates',
    static_folder ='static',
    static_url_path='/assets'

)
# ----------------- Add User Data  and login ------------------ #
    
@users_blueprint.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST': 
       
        useremail = request.form['useremail'] #asking user to fill out this form field
        username = request.form['username']
        userpassword = request.form['userpassword']
        userprofile = {'username': username, 'useremail': useremail, 'userpassword': userpassword}
        
        
        if mongo.db.users.find_one({"username": username, "useremail": useremail}): #checking mongodb for matching email
            return 'Sorry, this password has already been taken by someone else'
        else:
            mongo.db.users.insert_one(userprofile)
        session['username'] = request.form['username'] #sessions are important because of tracking a user
        return render_template('index.html', userprofile=userprofile, userpassword=userpassword)
    return render_template("auth/registration.html")

@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    username = session.get('username')
    if username:
        users = mongo.db.users.find()
        return render_template('profile.html', users=users)

    else:
        if request.method == 'POST':
    
            userpassword = request.form['userpassword'] #asking user to fill out this form field
            useremail = request.form["useremail"]
            
        
            userprofile = mongo.db.users.find_one({"username": username})
            userEmail = mongo.db.users.find_one({"useremail": useremail})

            if userprofile and userEmail and mongo.db.users.find_one({"userpassword": userpassword}):
        
                session["users"] = request.form.get("username")
                return render_template('add_message.html', username_profile=session["users"])
            else:
                return 'sorry wrong password or email'
    return render_template('auth/login.html')