from datetime import datetime
import logging
import edu_backend.config as config
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_restful import Api  # new

logger = logging.getLogger()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
ma = Marshmallow(app)