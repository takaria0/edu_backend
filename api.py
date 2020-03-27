from flask import Flask
import json
from flask_restful import reqparse, abort, Api, Resource
import config
import models.init_db as init_db
import flask_sqlalchemy



def create_app(db):

    flask_app = Flask(__name__)
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    print(config.SQLALCHEMY_DATABASE_URI)
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
    api = Api(flask_app)
    db.init_app(flask_app)
    flask_app.app_context().push()

    # print('---------------------------------------------------')
    # import os
    # import psycopg2

    # DATABASE_URL='postgresql://user:password@postgres:5432/edu_test'
    # print(DATABASE_URL)
    # print(config.SQLALCHEMY_DATABASE_URI)
    # cursor = psycopg2.connect(DATABASE_URL)
    # print(cursor)
    # print('---------------------------------------------------')

    db.create_all()
    return flask_app, api, db

def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task')


# Todo
# shows a single todo item and lets you delete a todo item
class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201



# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        print('Wahts going on')
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201

# get Test
# shows a list of all todos, and lets you POST to add new tasks

    # def post(self):
    #     args = parser.parse_args()
    #     todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
    #     todo_id = 'todo%i' % todo_id
    #     TODOS[todo_id] = {'task': args['task']}
    #     return TODOS[todo_id], 201

print('Hi')
app, api, db = create_app(init_db.db)

Test = init_db.Test

class TestHandler(Resource):
    def get(self):
        results = Test.query.all()
        [vars(r).pop("_sa_instance_state") for r in results]
        results = [vars(r) for r in results]
        return {
            "status": 200,
            "results": results,
        }

print('-----------------------aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
test = Test(content='aiueo')
db.session.add(test)
db.session.commit()

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}
##
## Actually setup the Api resource routing here
##
api.add_resource(TestHandler, '/test')
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
