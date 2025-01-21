# app.py (main application file)
import os
import secrets
from flask import Flask, session
from flask_cors import CORS
from flask_session import Session

# Create Flask Application
app  = Flask(__name__)

# Allow CORS for all domains
CORS(app)

# set the secret key for the session management
secret_key=secrets.token_hex(32)

# Inizialise the session
Session(app)

if __name__=='__main__':
    app.run(debug=True)