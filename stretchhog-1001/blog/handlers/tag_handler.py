import json

from flask import Response, request

from flask.ext.restful import Resource
from blog.forms import TagForm
from handler import Handler, root_blog_api
from main import api
from blog.services.tag_service import service
from blog.views import TagView
from blog.models import Tag


class TagHandler(Handler):
	def __init__(self, tag_service, form, view):
		super(TagHandler, self).__init__(tag_service, form, view)


handler = TagHandler(service, TagForm, TagView)


class TagRUD(Resource):
	@staticmethod
	def get(key):
		return handler.get_response_for(urlsafe=key)

	@staticmethod
	def delete(key):
		return handler.delete_response_for(key)

	@staticmethod
	def put(key):
		return handler.put_response_for(key, request)


class TagCL(Resource):
	@staticmethod
	def get():
		tags = service.get_all_tags()
		view = [TagView(tag).__dict__ for tag in tags]
		sorted_view = sorted(view, key=lambda t: t['category'])
		return Response(json.dumps(sorted_view), 200, mimetype='application/json')

	@staticmethod
	def post():
		return handler.post_response_for(request)


class TagBySlug(Resource):
	def get(self, slug):
		cat = service.get_by_slug(Tag, slug)
		return handler.get_response_for(key=cat.key)

tag = '/tag'
api.add_resource(TagRUD, root_blog_api + tag + '/<string:key>', endpoint='tag_rud')
api.add_resource(TagCL, root_blog_api + tag + '/', endpoint='tag_cl')

api.add_resource(TagBySlug, root_blog_api + tag + '/slug/<string:slug>', endpoint='tag_slug')
