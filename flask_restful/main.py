from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

# https://docs.sqlalchemy.org/en/14/core/dml.html
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # relative path
db = SQLAlchemy(app)

# test: if not work, check network or proxy
class HelloWorld(Resource):
    def get(self):
        return {"data": "Hello World"}
api.add_resource(HelloWorld, "/helloworld")

# model
class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video(title={title}, views={views}, likes={likes})"

# db.create_all() # only run once

# request parser
video_put_args = reqparse.RequestParser()  # better than using `request`, it can do validation
video_put_args.add_argument("title", type=str, required=True, help="Title of the video is required")
video_put_args.add_argument("views", type=int, required=True, help="Views of the video")
video_put_args.add_argument("likes", type=int, required=True, help="Likes on the video")

video_update_args = reqparse.RequestParser()  # better than using `request`, it can do validation
video_update_args.add_argument("title", type=str, help="Title of the video")
video_update_args.add_argument("views", type=int, help="Views of the video")
video_update_args.add_argument("likes", type=int, help="Likes on the video")

# for marshal_with
resource_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer
}

# helpers
def abort_if_video_id_not_exist(video_id):
    if not VideoModel.query.filter_by(id = video_id).first():
        abort(404, message="video id not exist")

def abort_if_video_id_already_exist(video_id):
    if VideoModel.query.filter_by(id = video_id).first():
        abort(409, message="video already exists with that id")

# resources
class Video(Resource):

    @marshal_with(resource_fields)  # when return model object, to serialize with fields
    def get(self, video_id):
        abort_if_video_id_not_exist(video_id)
        result = VideoModel.query.filter_by(id = video_id).first()
        return result, 200

    @marshal_with(resource_fields)
    def put(self, video_id):
        abort_if_video_id_already_exist(video_id)
        # test request
        # print(request.form)
        args = video_put_args.parse_args()
        video = VideoModel(id=int(video_id), title=args['title'], views=args['views'], likes=args['likes'])
        db.session.add(video)
        db.session.commit()
        return video, 201

    @marshal_with(resource_fields)
    def patch(self, video_id):
        abort_if_video_id_not_exist(video_id)
        video = VideoModel.query.filter_by(id = video_id).first()
        args = video_update_args.parse_args()
        if args.get('title', None):
            video.title = args['title']
        if args.get('view', None):
            video.views = args['views']
        if args.get('likes', None):
            video.likes = args['likes']
        db.session.commit()
        return video, 200

    @marshal_with(resource_fields)
    def delete(self, video_id):
        abort_if_video_id_not_exist(video_id)
        video = VideoModel.query.filter_by(id = video_id).first()
        db.session.delete(video)
        db.session.commit()
        return video, 204


api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
	app.run(debug=True)
