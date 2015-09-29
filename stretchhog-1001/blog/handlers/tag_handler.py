import json

from flask import Response, request

from flask.ext.restful import Resource
from forms import TagForm
from handler import Handler
from main import api
from tag_service import service
from views import TagView


class TagHandler(Handler):
	def __init__(self, tag_service, form, view):
		super(TagHandler, self).__init__(tag_service, form, view)


handler = TagHandler(service, TagForm, TagView)


class TagRUD(Resource):
	@staticmethod
	def get(self, key):
		return handler.get_response_for(key)

	@staticmethod
	def delete(self, key):
		return handler.delete_response_for(key)

	@staticmethod
	def put(self, key):
		return handler.put_response_for(key, request)


class TagCL(Resource):
	@staticmethod
	def get(self):
		tags = service.get_all_tags()
		view = [TagView(tag).__dict__ for tag in tags]
		sorted_view = sorted(view, key=lambda t: t['category'])
		return Response(json.dumps(sorted_view), 200, mimetype='application/json')

	@staticmethod
	def post(self):
		return handler.post_response_for(request)


api.add_resource(TagRUD, '/blog/admin/tag/<string:key>', endpoint='tag_rud')
api.add_resource(TagCL, '/blog/admin/tag', endpoint='tag_cl')
