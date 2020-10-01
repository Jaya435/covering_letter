#/src/views/SectionView.py
from flask import request, g, Blueprint, json, Response
from ..models.SectionModel import SectionModel, SectionSchema

blogpost_api = Blueprint('blogpost_api', __name__)
blogpost_schema = SectionSchema()


@blogpost_api.route('/', methods=['POST'])
def create():
  """
  Create Blogpost Function
  """
  req_data = request.get_json()
  data = blogpost_schema.load(req_data)
  post = SectionModel(data)
  post.save()
  data = blogpost_schema.dump(post)
  return custom_response(data, 201)

@blogpost_api.route('/', methods=['GET'])
def get_all():
  """
  Get All Blogposts
  """
  posts = SectionModel.get_all_blogposts()
  data = blogpost_schema.dump(posts, many=True)
  return custom_response(data, 200)


@blogpost_api.route('/<int:blogpost_id>', methods=['PUT'])
def update(blogpost_id):
  """
  Update A Blogpost
  """
  req_data = request.get_json()
  post = SectionModel.get_one_blogpost(blogpost_id)
  if not post:
    return custom_response({'error': 'post not found'}, 404)
  data = blogpost_schema.dump(post)
  if data.get('owner_id') != g.user.get('id'):
    return custom_response({'error': 'permission denied'}, 400)

  data= blogpost_schema.load(req_data, partial=True)
  post.update(data)

  data = blogpost_schema.dump(post)
  return custom_response(data, 200)

@blogpost_api.route('/<int:blogpost_id>', methods=['DELETE'])
def delete(blogpost_id):
  """
  Delete A Blogpost
  """
  post = SectionModel.get_one_blogpost(blogpost_id)
  if not post:
    return custom_response({'error': 'post not found'}, 404)
  data = blogpost_schema.dump(post)

  post.delete()
  return custom_response({'message': 'deleted'}, 204)


def custom_response(res, status_code):
  """
  Custom Response Function
  """
  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
  )