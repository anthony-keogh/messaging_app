import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from wtforms.validators import (DataRequired, Email,EqualTo,Length,URL)
from wtforms import Form, BooleanField, StringField, PasswordField, validators
import os
from datetime import datetime

from flask import session
from werkzeug.security import check_password_hash, generate_password_hash


app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

if os.path.isfile('env.py'):
    import env


#mongodb atlas connection below

app.config["MONGO_DBNAME"] = os.environ.get('MONGO_DBNAME')
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)
#app.secret_key = 'super secret key'





# ----------------- Routes to Pages ------------------ #
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/getting_started')
def getting_started():
    return render_template('getting_started.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/mission')
def mission():
    return render_template('mission.html')

@app.route('/team')
def team():
    return render_template('team.html')



@app.route('/message')
def message():
    message = mongo.db.messageappmicrosoft.message.find_one()
    return render_template('message.html', message=message)
    
@app.route('/messages')
def messages():
    message = mongo.db.messageappmicrosoft.message.find_one()
    channel = mongo.db.messageappmicrosoft.channel.find_one()
    return render_template('messages.html', message=message, channel=channel)

@app.route('/channels')
def channels():
    channel = mongo.db.messageappmicrosoft.channel.find_one()
    return render_template('channels.html', channel=channel)

@app.route('/channel')
def channel():
    channel = mongo.db.messageappmicrosoft.channel.find_one()
    return render_template('channel.html', channel=channel)






# ----------------- Add User Data  and login ------------------ #


        
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST': 
       
        useremail = request.form['useremail'] #asking user to fill out this form field
        username = request.form['username']
        userpassword = request.form['userpassword']
        userprofile = {'username': username, 'useremail': useremail, 'userpassword': userpassword}
        
        
        if mongo.db.messageappmicrosoft.users.find_one({"username": username, "useremail": useremail}): #checking mongodb for matching email
            return 'Sorry, this password has already been taken by someone else'
        else:
            mongo.db.messageappmicrosoft.users.insert_one(userprofile)
        session['username'] = request.form['username'] #sessions are important because of tracking a user
        return render_template('index.html', userprofile=userprofile, userpassword=userpassword)
    return render_template("auth/registration.html")

@app.route('/login', methods=["GET", "POST"])
def login():
    username = session.get('username')
    if username:
        users = mongo.db.users.find()
        return render_template('index.html', users=users)

    if request.method == 'POST':
        
        userpassword = request.form['userpassword'] #asking user to fill out this form field
        useremail = request.form["useremail"]
        

        userprofile = mongo.db.messageappmicrosoft.users.find({"username": username})
        userEmail = mongo.db.messageappmicrosoft.users.find({"useremail": useremail})
        if userprofile and userEmail and mongo.db.messageappmicrosoft.users.find({"userpassword": userpassword}):
        
            session["users"] = request.form.get("username")
            return render_template('add_message.html', username_profile=session["users"])
        else:
            return 'sorry wrong password or email'
    return render_template('auth/login.html')






# ----------------- Channel ------------------ #

@app.route('/create_channel')
def create_channel():
    channel_Add = channel = mongo.db.messageappmicrosoft.channel.find()  #gaining access to mongodb atlas database and able to find items inside the collection
    return render_template('create_channel.html', channel_Add=channel_Add)


@app.route('/adding_channels/', methods=['GET', 'POST'])
def adding_channels():
    channel_add_var = channel = mongo.db.messageappmicrosoft.channel.find()  #gaining access to mongodb atlas database and able to find items inside the collection
    channel_add_var.insert_one({
     
                        'channel_Name': request.form.get('channel_Name'), #asking user to fill out this form field
                        'channel_Description': request.form.get('channel_Description'),
                        'username_channel': request.form.get('username_channel'),
   })
    
    return redirect(url_for('channels'))









# ----------------- message ------------------ #



@app.route('/add_message')
def add_message():
    message_Add = mongo.db.messageappmicrosoft.message.find()  #gaining access to mongodb atlas database and able to find items inside the collection
    return render_template("add_message.html",  message_Add=message_Add)

@app.route('/adding_message/', methods=['GET', 'POST'])
def adding_messages():
    today = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    message_add_var = mongo.db.messageappmicrosoft.message  #gaining access to mongodb atlas database and able to find items inside the collection
    message_add_var.insert_one({
     
                        'message_Description': request.form.get('message_Description'), #asking user to fill out this form field
                        'summary': request.form.get('summary'),
                        'username': request.form.get('username'),
                        "date_added": today,
                        
                        
   })
    
    return redirect(url_for('messages'))

# ----------------- Edit message Data ------------------ #

@app.route('/edit_message/<message_id>')
def editOne(message_id):
    editMessage = mongo.db.messageappmicrosoft.find_one( {"_id": ObjectId("message")}) #gaining access to mongodb atlas database and able to find id of the collection
    return render_template('edit_message.html', editMessage=editMessage)

@app.route('/update_message/<message_id>', methods=['GET', 'POST'])
def updateOne(message_id):
   today = datetime.now().strftime("%d %B, %Y")
   updateMessage = mongo.db.messageappmicrosoft #gaining access to mongodb atlas database and able to find items inside the collection
   updateMessage.update({"_id": ObjectId("message")},
       				 {
       					'message_Description': request.form.get('message_Description'), #asking user to fill out this form field
                        'Summary_Title': request.form.get('Summary_Title'),
                        'username': request.form.get('username'),
                        "date_added": today,
                        
                   },)
   return redirect(url_for('edit_message', updateMessage=updateMessage))

# ----------------- Remove message Data ------------------ #
@app.route('/delete_message/<message_id>')
def deleteOne(message_id):
   mongo.db.messageappmicrosoft.remove({"_id": ObjectId("message")})  #gaining access to mongodb atlas database and able to find id of the collection

@app.route('/delete_all')
def deleteAll():
   mongo.db.messageappmicrosoft.remove()




if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=False)