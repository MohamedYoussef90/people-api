import os
import connexion
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

base_dir = os.path.abspath(os.path.dirname(__file__))

# Create connexion app instance
connex_app = connexion.App(__name__, specification_dir=base_dir)

# Get the underlying Flask app
app = connex_app.app

# Configure SQLAlchemy part of the app instance
# Echo SQL statements it executes to the console (useful for debugging db programs)
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'people.db')
# Disable tracking modifications, as it's not typically needed for SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create the SQLAlchemy db instance
db = SQLAlchemy(app)

# Initialize Marshmallow
ma = Marshmallow(app)

# Create an application context
with app.app_context():
    # You can now perform database operations safely within this context
    db.create_all()  # For example, create database tables

# Rest of your code
