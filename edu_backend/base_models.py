from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from edu_backend.app import app
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand, init, migrate, upgrade

db = SQLAlchemy(app)
Migrate(app, db)

# manager = Manager(app)
# manager.add_command('db', MigrateCommand)
# Base = declarative_base()

# import models here
from edu_backend.models.course import Course, CourseSchema
from edu_backend.models.course_detail import CourseDetail, CourseDetailSchema
from edu_backend.models.tests_post import TestPost, TestPostSchema
# engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
# db.Model.metadata.create_all(engine)
# db.create_all()
# Session = sessionmaker(bind=engine)
# session = Session()



###############################
## Migration
## Coming Soon!
###############################
# with app.app_context():
#   init(directory='migrations', multidb=False)
#   migrate(directory='migrations')
#   upgrade(directory='migrations')
