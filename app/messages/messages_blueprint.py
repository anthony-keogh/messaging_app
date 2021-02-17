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
#from app.utils import message_collection, channel_collection

messages_blueprint = Blueprint("messages_blueprint", __name__,

    template_folder ='templates',
    static_folder ='static', 
    static_url_path='/assets'
)


#----------- messages ------------------#

@messages_blueprint.route('/message/<message_id>')
def view_message(message_id):
    message = mongo.db.message.find_one( {"_id": ObjectId(message_id)})
    return render_template('message.html', message=message)

@messages_blueprint.route('/messages', methods=['GET'])
def messages():
    messages_All = mongo.db.message.find()
    channel_Name = mongo.db.channel.find()
    return render_template('messages.html', messages_All=messages_All, channel_Name=channel_Name)



# ----------------- message ------------------ #



@messages_blueprint.route('/add_message')
def add_message():
    message_Add = mongo.db.message.find()
    channel_Name= mongo.db.channel.find()
     
    users = mongo.db.users.find()                                                                                   #find channel 

      #gaining access to mongodb atlas database and able to find items inside the collection
    return render_template("add_message.html",  message_Add=message_Add, channel_Name=channel_Name, users=users)

@messages_blueprint.route('/adding_message/', methods=['GET', 'POST'])
def adding_messages():
    today = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    message_add_var = mongo.db.message
    all_channel = mongo.db.channel 
                                                                                           #find channel
     
    both_message_channel = all_channel and message_add_var
    
      #gaining access to mongodb atlas database and able to find items inside the collection
    both_message_channel.insert_one({
     
                        'message_Description': request.form.get('message_Description'), #asking user to fill out this form field
                        'summary': request.form.get('summary'),
                        'username': request.form.get('username'),
                        "date_added": today,
                        'channel_Name': request.form.get('selectpicker'),
                        'username': request.form.get('selectpicker')
                        
   })
    return redirect(url_for('messages'))

# ----------------- Edit message Data ------------------ #

@messages_blueprint.route('/edit_message/<message_id>')
def editOne(message_id):
    editMessage = mongo.db.message.find_one( {"_id": ObjectId("message")}) #gaining access to mongodb atlas database and able to find id of the collection
    return render_template('edit_message.html', editMessage=editMessage)

@messages_blueprint.route('/update_message/<message_id>', methods=['GET', 'POST'])
def updateOne(message_id):
   today = datetime.now().strftime("%d %B, %Y")
   updateMessage = mongo.db.message #gaining access to mongodb atlas database and able to find items inside the collection
   updateMessage.update({"_id": ObjectId("message")},
       				 {
       					'message_Description': request.form.get('message_Description'), #asking user to fill out this form field
                        'Summary_Title': request.form.get('Summary_Title'),
                        'username': request.form.get('username'),
                        "date_added": today,
                        
                   },)
   return redirect(url_for('edit_message', updateMessage=updateMessage))

# ----------------- Remove message Data ------------------ #
@messages_blueprint.route('/delete_message/<message_id>')
def deleteOne(message_id):
   mongo.db.messageremove({"_id": ObjectId("message")})  #gaining access to mongodb atlas database and able to find id of the collection

@messages_blueprint.route('/delete_all')
def deleteAll():
   mongo.db.message.remove()