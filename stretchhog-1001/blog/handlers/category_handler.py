import json

from blog.services.category_service import service
from flask import request, Response

from flask.ext.restful import Resource
from forms import CategoryForm
from handler import Handler
from main import api
from views import CategoryView


class CategoryHandler(Handler):
	def __init__(self, category_service, form, view):
		super(CategoryHandler, self).__init__(category_service, form, view)


handler = CategoryHandler(service, CategoryForm, CategoryView)


class CategoryRUD(Resource):
	@staticmethod
	def get(self, key):
		return handler.get_response_for(key)

	@staticmethod
	def delete(self, key):
		return handler.delete_response_for(key)

	@staticmethod
	def put(self, key):
		return handler.put_response_for(key, request)


class CategoryCL(Resource):
	@staticmethod
	def get(self):
		categories = service.get_all_categories()
		view = [CategoryView(cat).__dict__ for cat in categories]
		return Response(json.dumps(view), 200, mimetype='application/json')

	@staticmethod
	def post(self):
		return handler.post_response_for(request)

api.add_resource(CategoryRUD, '/blog/admin/category/<string:key>', endpoint='category_rud')
api.add_resource(CategoryCL, '/blog/admin/category', endpoint='category_cl')

