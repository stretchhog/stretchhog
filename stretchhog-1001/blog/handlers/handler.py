import json

from flask import Response, request
from flask.ext.restful import Resource
from main import api
from blog.views import MarkdownPreviewView

root_blog_api = '/blog-api'


class Handler(object):
	def __init__(self, service, form, view):
		self.service = service
		self.form = form
		self.view = view

	def get_response_for(self, key):
		entity = self.service.get_by_urlsafe_key(key)
		view = self.view(entity).__dict__
		return Response(json.dumps(view), 200, mimetype='application/json')

	def put_response_for(self, key, req):
		form = self.get_form(req)
		if form.validate():
			key = self.service.update(key, form)
			view = self.view(key.get()).__dict__
			return Response(json.dumps(view), 200, mimetype='application/json')
		else:
			view = self.view.from_form(form)
			return Response(json.dumps(view), status=400, mimetype='application/json')

	def delete_response_for(self, key):
		self.service.delete(key)
		return Response(status=204)

	def post_response_for(self, req):
		form = self.get_form(req)
		if form.validate():
			key = self.service.create(form)
			view = self.view(key.get()).__dict__
			return Response(json.dumps(view), 201, mimetype='application/json')
		else:
			view = self.view.from_form(form)
			return Response(json.dumps(view), status=400, mimetype='application/json')

	def get_form(self, req):
		return self.form.from_json(req.get_json())


class MarkdownPreview(Resource):
	@staticmethod
	def post(self):
		view = MarkdownPreviewView(request.get_json()['preview']).__dict__
		return Response(json.dumps(view), 200, mimetype='application/json')


api.add_resource(MarkdownPreview, root_blog_api + '/markdown/preview', endpoint='markdown_preview')
