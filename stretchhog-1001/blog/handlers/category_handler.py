import json
from blog.services.category_service import service
from flask import request, Response
from flask.ext.restful import Resource
from blog.forms import CategoryForm
from blog.handlers.handler import Handler, root_blog_api
from main import api
from blog.views import CategoryView, CategorySummaryView


class CategoryHandler(Handler):
	def __init__(self, category_service, form, view):
		super(CategoryHandler, self).__init__(category_service, form, view)


handler = CategoryHandler(service, CategoryForm, CategoryView)


class CategoryRUD(Resource):
	@staticmethod
	def get(key):
		return handler.get_response_for(key)

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


api.add_resource(CategoryRUD, root_blog_api + '/category/<string:key>', endpoint='category_rud')
api.add_resource(CategoryCL, root_blog_api + '/category', endpoint='category_cl')

api.add_resource(Categories, root_blog_api + '/categories', endpoint='categories')
