from flask import Response

from blog.services.comment_service import service
from flask.ext.restful import Resource, request
from blog.forms import CommentForm
from blog.handlers.handler import Handler
from main import api
from blog.views import CommentView


class CommentHandler(Handler):
	def __init__(self, comment_service, form, view):
		super(CommentHandler, self).__init__(comment_service, form, view)


handler = CommentHandler(service, CommentForm, CommentView)


class CommentRUD(Resource):
	@staticmethod
	def get(self, key):
		return handler.get_response_for(urlsafe=key)

	@staticmethod
	def delete(self, key):
		return handler.delete_response_for(key)


class CommentCL(Resource):
	@staticmethod
	def post(self):
		return handler.post_response_for(request)


class CommentApprove(Resource):
	@staticmethod
	def put(self, key):
		service.approve_comment(key)
		return Response(status=204)


class CommentSpam(Resource):
	@staticmethod
	def put(self, key):
		service.spam_comment(key)
		return Response(status=204)


api.add_resource(CommentRUD, '/blog-api/comment/<string:key>', endpoint='comment_rud')
api.add_resource(CommentCL, '/blog-api/comment', endpoint='comment_cl')

api.add_resource(CommentApprove, '/blog-api/comment/<string:key>', endpoint='comment_approve')
api.add_resource(CommentSpam, '/blog-api/spam/<string:key>', endpoint='comment_spam')
