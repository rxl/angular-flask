from angular_flask import app

from flask_sqlalchemy import SQLAlchemy
from flask_restless import APIManager

db = SQLAlchemy(app)

api_manager = APIManager(app, flask_sqlalchemy_db=db)
