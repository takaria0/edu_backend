from datetime import datetime
import logging
import os
import edu_backend.config as config
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource  # new

logger = logging.getLogger()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
api = Api(app)
ma = Marshmallow(app)