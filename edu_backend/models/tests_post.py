from datetime import datetime
from ..app import ma
from edu_backend.base_models import db
from sqlalchemy import *
from sqlalchemy.orm import relationship

#########################################
# Model
#########################################

class TestPost(db.Model):
    __tablename__ = 'test_posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    content = Column(String(255))

    def __repr__(self):
        return '<Post %s>' % self.title



#########################################
# Serializer
#########################################


class TestPostSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "content")
