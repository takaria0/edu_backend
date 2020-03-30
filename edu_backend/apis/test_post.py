from edu_backend.base_models import db, TestPost, TestPostSchema
from flask import request, Response, abort, jsonify
from flask_restful import Resource

# init Schema
post_schema = TestPostSchema()
posts_schema = TestPostSchema(many=True)

#########################################
# Routes to handle API
#########################################


class PostListResource(Resource):
    def get(self):
        posts = db.session.query(TestPost).all()
        return posts_schema.dump(posts)

    # new
    def post(self):
        new_post = TestPost(
          title=request.json['title'],
          content=request.json['content']
        )

        try:
          db.session.add(new_post)
          db.session.commit()
        except:
          db.session.rollback()
        finally:
          # session.close()
          pass

        return post_schema.dump(new_post)

# try:
#     # first query.  a Connection is acquired
#     # from the Engine, and a Transaction
#     # started.
#     item1 = session.query(Item).get(1)

#     # second query.  the same Connection/Transaction
#     # are used.
#     item2 = session.query(Item).get(2)

#     # pending changes are created.
#     item1.foo = 'bar'
#     item2.bar = 'foo'

#     # commit.  The pending changes above
#     # are flushed via flush(), the Transaction
#     # is committed, the Connection object closed
#     # and discarded, the underlying DBAPI connection
#     # returned to the connection pool.
#     session.commit()
# except:
#     # on rollback, the same closure of state
#     # as that of commit proceeds.
#     session.rollback()
#     raise
# finally:
#     # close the Session.  This will expunge any remaining
#     # objects as well as reset any existing SessionTransaction
#     # state.  Neither of these steps are usually essential.
#     # However, if the commit() or rollback() itself experienced
#     # an unanticipated internal failure (such as due to a mis-behaved
#     # user-defined event handler), .close() will ensure that
#     # invalid state is removed.
#     session.close()
