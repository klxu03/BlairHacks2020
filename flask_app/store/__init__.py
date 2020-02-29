# This is the initiation file that creates our module, here we configure our application
# Import flask
from flask import Flask
# Import ssl forcer
#from flask_sslify import SSLify
# Import sessions
from flask_session import Session
# Import the os module
import os
# Import CSRF protection
from flask_wtf.csrf import CSRFProtect
# Import libraries for limits on external uploads in Flask forms
#from flask.ext.uploads import UploadSet, IMAGES

# Create the flask app
app = Flask(__name__)

# Configure the secret key, which is needed for the application
app.config['SECRET_KEY'] = 'SECRET_KEY'
# Set the session type to filesystem because the default system won't work for our purposes
app.config['SESSION_TYPE'] = 'filesystem'
# Active sessions for the app
Session(app)
# Activate csrf protection
csrf = CSRFProtect(app)
# Add ssl
#SSLify(app)

# Configure the image uploading 
#images = UploadSet('images', IMAGES)
# Store the configuration of the Flask-Uploads module in the Flask application
#configure_uploads(app, images)

# Import the routes here 
from store import routes
