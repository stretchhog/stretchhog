from requests import request

from comment_service import service
from flask.ext.restful import Resource
from forms import CommentForm
from handler import Handler
from main import api
from views import CommentView


class CommentHandler(Handler):
	def __init__(self, comment_service, form, view):
		super(CommentHandler, self).__init__(comment_service, form, view)


handler = CommentHandler(service, CommentForm, CommentView)


class CommentRUD(Resource):
	@staticmethod
	def get(self, key):
		return handler.get_response_for(key)

	@staticmethod
	def delete(self, key):
		return handler.delete_response_for(key)


class CommentCL(Resource):
	@staticmethod
	def post(self):
		return handler.post_response_for(request)


api.add_resource(CommentRUD, '/blog/admin/comment/<string:key>', endpoint='comment_rud')
api.add_resource(CommentCL, '/blog/admin/comment', endpoint='comment_cl')
