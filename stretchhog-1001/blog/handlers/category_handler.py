import json

from blog.forms import CategoryForm
from blog.handlers.handler import Handler, blog_api_root, admin_blog_root, category
from blog.services.category_service import service
from blog.views import CategoryView, CategorySummaryView
from blog.models import Category
from flask import request, Response
from flask.ext.restful import Resource
from main import api


class CategoryHandler(Handler):
	def __init__(self, category_service, form, view):
		super(CategoryHandler, self).__init__(category_service, form, view)


handler = CategoryHandler(service, CategoryForm, CategoryView)


class CategoryRUD(Resource):
	@staticmethod
	def get(key):
		return handler.get_response_for(urlsafe=key)

	@staticmethod
	def delete(key):
		return handler.delete_response_for(key)

	@staticmethod
	def put(key):
		return handler.put_response_for(key, request)


class CategoryCL(Resource):
	@staticmethod
	def get():
		categories = service.get_all_categories()
		view = [CategoryView(cat).__dict__ for cat in categories]
		return Response(json.dumps(view), 200, mimetype='application/json')

	@staticmethod
	def post():
		return handler.post_response_for(request)


class Categories(Resource):
	@staticmethod
	def get():
		categories = service.get_all_categories()
		view = [CategorySummaryView(cat).__dict__ for cat in categories]
		return Response(json.dumps(view), 200, mimetype='application/json')


class CategoryBySlug(Resource):
	def get(self, slug):
		cat = service.get_by_slug(Category, slug)
		return handler.get_response_for(key=cat.key)


api.add_resource(CategoryRUD, admin_blog_root + category + '/<string:key>', endpoint='category_rud')
api.add_resource(CategoryCL, admin_blog_root + category, endpoint='category_cl')

api.add_resource(Categories, blog_api_root + category + '/list', endpoint='category_list')
api.add_resource(CategoryBySlug, blog_api_root + category + '/slug/<string:slug>', endpoint='category_slug')
