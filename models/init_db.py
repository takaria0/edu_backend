import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()



class Test(db.Model):
  __tablename__ = "test"
  id = db.Column(db.Integer, primary_key=True)
  content = db.Column(db.String(100))
