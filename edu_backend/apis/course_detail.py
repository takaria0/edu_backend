from edu_backend.base_models import db, CourseDetail, CourseDetailSchema
from flask import request, Response, abort, jsonify
from flask_restful import Resource

# init Schema
course_schema = CourseDetailSchema()
courses_schema = CourseDetailSchema(many=True)

#########################################
# Routes to handle API
#########################################


class CourseDetailResource(Resource):
    def get(self):
        posts = db.session.query(CourseDetail).all()
        return courses_schema.dump(posts)

    # new
    def post(self):
        new_post = CourseDetail(
          course_id=request.json['course_id'],
          week=request.json['week'],
          content=request.json['content'],
          video_url=request.json['video_url'],
        )
        try:
          db.session.add(new_post)
          db.session.commit()
        except:
          db.session.rollback()
        finally:
          # session.close()
          pass
        return course_schema.dump(new_post)
