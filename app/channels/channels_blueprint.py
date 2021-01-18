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

from flask import jsonify
from flask import session
from app import mongo
from flask import (
    Blueprint, render_template, redirect,
    request, url_for, flash, session, Markup)
from werkzeug.security import check_password_hash, generate_password_hash



channels_blueprint = Blueprint("channels_blueprint ", __name__,

    template_folder ='templates',
    static_folder ='static', 
    static_url_path='/assets'
)




#----------- channel page ------------------#

@channels_blueprint.route('/channels/', methods=['GET'])
def channels():
  
  
  channel_Name = mongo.db.channel.find()         
  
  return render_template('channels.html' , channel_Name=channel_Name   )  


@channels_blueprint.route('/channel/<channel_id>')
def view_channel(channel_id):
    channel_Name = mongo.db.channel.find()
    channel = mongo.db.channel.find_one( {"_id": ObjectId(channel_id)})
    messages_All = mongo.db.message.find()
   
    return render_template('channel.html', channel=channel, messages_All=messages_All, channel_Name=channel_Name )





# ----------------- Channel ------------------ #

@channels_blueprint.route('/create_channel')
def create_channel():
    channel_Add = mongo.db.channel.find()  #gaining access to mongodb atlas database and able to find items inside the collection
    
    return render_template('create_channel.html', channel_Add=channel_Add)

#channel_Add = mongo.db.messageappmicrosoft.channel.find()

@channels_blueprint.route('/adding_channels/', methods=['GET', 'POST'])
def adding_channels():
    channel_add_var = mongo.db.channel
    today = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
      #gaining access to mongodb atlas database and able to find items inside the collection
    channel_add_var.insert_one({
     
                        'channel_Name': request.form.get('channel_Name'), #asking user to fill out this form field
                        'channel_Description': request.form.get('channel_Description'),
                        'username_channel': request.form.get('username_channel'),
                        'channel_User_Job_Title': request.form.get('channel_User_Job_Title'),
                        'channel_User_Work_Experience': request.form.get('channel_User_Work_Experience'),
                        "date_added": today,
                        
   })
    
    return redirect(url_for('channels'))