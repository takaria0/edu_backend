from datetime import datetime
from ..app import ma
from edu_backend.base_models import db, Course
from sqlalchemy import *
from sqlalchemy.orm import relationship


#########################################
# Model
#########################################

class CourseDetail(db.Model):
    __tablename__ = 'course_detail'
    id = Column(Integer,
                          primary_key=True)
    week = Column(Integer)
    content = Column(String(10000))
    video_url = Column(String(500))
    updated_at = Column(DateTime,
                          default=datetime.utcnow(),
                          onupdate=datetime.utcnow())
    created_at = Column(DateTime,
                          default=datetime.utcnow())
    
    # relation
    course_id = Column(Integer, ForeignKey('course.id'))

#########################################
# Serializer
#########################################

class CourseDetailSchema(ma.Schema):
    class Meta:
      fields = ('id', 'course_id', 'week', 'content', 'video_url', 'updated_at', 'created_at')
