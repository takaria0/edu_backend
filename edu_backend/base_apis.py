import os
from edu_backend.app import api, app
from edu_backend.apis.test_post import PostListResource
from edu_backend.apis.course import CourseResource
from edu_backend.apis.course_detail import CourseDetailResource

@app.route('/')
def hello_world():
    target = os.environ.get('TARGET', 'World')
    return {
      "message": 'Hello {}!\n'.format(target),
      "content": "Hi",
    }



api.add_resource(PostListResource, '/post')
api.add_resource(CourseResource, '/course')
api.add_resource(CourseDetailResource, '/course_detail')
