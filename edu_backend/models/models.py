from datetime import datetime
from ..app import db, ma

class Test(db.Model):
  __tablename__ = "test"
  id = db.Column(db.Integer, primary_key=True)
  content = db.Column(db.String(100))

#########################################
# Model (DB) and Schema (Serialization)
#########################################

#########################################
# Person
#########################################

class Person(db.Model):
    __tablename__ = 'person'
    person_id = db.Column(db.Integer,
                          primary_key=True)
    lname = db.Column(db.String)
    fname = db.Column(db.String)
    timestamp = db.Column(db.DateTime,
                          default=datetime.utcnow(),
                          onupdate=datetime.utcnow())

class PersonSchema(ma.Schema):
    class Meta:
        model = Person
        sqla_session = db.session


#########################################
# Product
#########################################

class Product(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)

    def __init__(self, name, description, price, qty):
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty


class ProductSchema(ma.Schema):
    class Meta:
        fields = ('_id', 'name', 'description', 'price', 'qty')


#########################################
# Post
#########################################

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    content = db.Column(db.String(255))

    def __repr__(self):
        return '<Post %s>' % self.title


class PostSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "content")
