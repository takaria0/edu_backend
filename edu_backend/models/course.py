from datetime import datetime
from ..app import ma
from edu_backend.base_models import db
from sqlalchemy import *
from sqlalchemy.orm import relationship

#########################################
# Model
#########################################

class Course(db.Model):
    __tablename__ = 'course'
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    description = Column(String(1000))
    updated_at = Column(DateTime,
                          default=datetime.utcnow(),
                          onupdate=datetime.utcnow())
    created_at = Column(DateTime,
                          default=datetime.utcnow())

    # relation
    details = relationship('CourseDetail', backref='course')

#########################################
# Serializer
#########################################

class CourseSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'updated_at', 'created_at')
