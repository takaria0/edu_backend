from datetime import datetime
import logging
import os
import config
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, Response, abort, jsonify
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource  # new

logger = logging.getLogger()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)
api = Api(app)
ma = Marshmallow(app)

#########################################
# Model (DB) and Schema (Serialization)
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


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    content = db.Column(db.String(255))

    def __repr__(self):
        return '<Post %s>' % self.title


class PostSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "content")


db.create_all()

# init Schema
post_schema = PostSchema()
posts_schema = PostSchema(many=True)


#########################################
# Routes to handle API
#########################################
class PostListResource(Resource):
    def get(self):
        posts = Post.query.all()
        return posts_schema.dump(posts)

    # new
    def post(self):
        new_post = Post(
            title=request.json['title'],
            content=request.json['content']
        )
        db.session.add(new_post)
        db.session.commit()
        return post_schema.dump(new_post)

@app.route('/')
def hello_world():
    target = os.environ.get('TARGET', 'World')
    return {
      "message": 'Hello {}!\n'.format(target),
      "content": "Hi",
    }

api.add_resource(PostListResource, '/posts')


if __name__ == "__main__":
    logger.info('Hi, This Server is now running.')
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
