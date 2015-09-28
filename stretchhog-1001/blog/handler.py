from google.appengine.ext.db import put
from google.appengine.ext.ndb.key import Key
import time
from blog.forms import CategoryForm, TagForm, EntryForm, CommentForm
from blog.models import Entry, Category, Comment
from flask import make_response, render_template, request, Response
from blog import service
from blog.views import TagView, CategoryView, EntryView, CommentView, EntryPostView
from flask.ext.restful import Resource
from main import api
from flask import Markup, json
import markdown

categories = {1: "Music", 2: "Artificial Intelligence", 3: "Fitness & Health"}


def get_response_for(key, view):
	entity = service.get_by_urlsafe_key(key)
	view = view(entity).__dict__
	return Response(json.dumps(view), 201, mimetype='application/json')


def put_response_for(key, view, form, update_function):
	if form.validate():
		key = update_function(key, form)
		view = view(key.get()).__dict__
		return Response(json.dumps(view), 201, mimetype='application/json')
	else:
		return Response(status=400, mimetype='application/json')


def delete_response_for(key, delete_function):
	delete_function(key)
	return Response(status=201)


def post_response_for(form, view, create_function):
	if form.validate():
		key = create_function(form)
		view = view(key.get()).__dict__
		return Response(json.dumps(view), 201, mimetype='application/json')
	else:
		return Response(status=400, mimetype='application/json')


def template_response_for(template):
	return make_response(render_template(template))


def get_form(form, req, put_mode=False):
	return form.from_json(req.get_json(), put_mode=put_mode)


class EntryTemplate(Resource):
	def get(self):
		return template_response_for('blog/entry/entryCRUD.html')


class EntryRUD(Resource):
	def get(self, key):
		entry = service.get_by_urlsafe_key(key)
		entry.post = Markup(markdown.markdown(entry.post))
		view = EntryView(entry).__dict__
		return Response(view, 200, mimetype='application/json')

	def put(self, key):
		return put_response_for(key, EntryView, get_form(EntryForm, request, put_mode=True), service.update_entry)

	def delete(self, key):
		return delete_response_for(key, service.delete_entry)


class EntryCL(Resource):
	def get(self):
		entries = service.get_all_entries()
		view = [EntryView(entry).__dict__ for entry in entries]
		return Response(json.dumps(view), 200, mimetype='application/json')

	def post(self):
		post_response_for(get_form(EntryForm, request), EntryView, service.create_entry)


class EntryPost(Resource):
	def get(self, key):
		entry = service.get_by_urlsafe_key(key)
		view = EntryPostView(entry).__dict__
		return Response(json.dumps(view), 200, mimetype='application/json')


class CategoryTemplate(Resource):
	def get(self):
		return template_response_for('blog/category/categoryCRUD.html')


class CategoryRUD(Resource):
	def get(self, key):
		return get_response_for(key, CategoryView)

	def delete(self, key):
		return delete_response_for(key, service.delete_category)

	def put(self, key):
		return put_response_for(key, CategoryView, get_form(CategoryForm, request), service.update_category)


class CategoryCL(Resource):
	def get(self):
		categories = service.get_all_categories()
		view = [CategoryView(cat).__dict__ for cat in categories]
		return Response(json.dumps(view), 200, mimetype='application/json')

	def post(self):
		return post_response_for(get_form(CategoryForm, request), CategoryView, service.create_category)


class TagTemplate(Resource):
	def get(self):
		return template_response_for('blog/tag/tagCRUD.html')


class TagRUD(Resource):
	def get(self, key):
		return get_response_for(key, TagView)

	def put(self, key):
		return put_response_for(key, TagView, get_form(TagForm, request, put_mode=True), service.update_tag)

	def delete(self, key):
		return delete_response_for(key, service.delete_tag)


class TagCL(Resource):
	def get(self):
		tags = service.get_all_tags()
		view = [TagView(tag).__dict__ for tag in tags]
		sorted_view = sorted(view, key=lambda t: t['category'])
		return Response(json.dumps(sorted_view), 200, mimetype='application/json')

	def post(self):
		return post_response_for(get_form(TagForm, request), TagView, service.create_tag)


class CommentRUD(Resource):
	def put(self, key):
		return put_response_for(key, CommentView, get_form(CommentForm, request, put_mode=True), service.update_comment)


class CommentC(Resource):
	def post(self):
		return post_response_for(get_form(CommentForm, request), CommentView, service.create_comment)


class AIMain(Resource):
	def get(self):
		return template_response_for('blog/entry/ai/main.html')


class MusicMain(Resource):
	def get(self):
		return template_response_for('blog/entry/music/main.html')


class FitnessMain(Resource):
	def get(self):
		return template_response_for('blog/entry/fitness/main.html')


api.add_resource(EntryRUD, '/blog/admin/entry/<string:key>', endpoint='entry_rud')
api.add_resource(EntryCL, '/blog/admin/entry', endpoint='entry_cl')
api.add_resource(EntryTemplate, '/blog/admin/entry/template', endpoint='entry_template')
api.add_resource(EntryPost, '/blog/admin/entry/post/<string:key>', endpoint='entry_post')

api.add_resource(CategoryRUD, '/blog/admin/category/<string:key>', endpoint='category_rud')
api.add_resource(CategoryCL, '/blog/admin/category', endpoint='category_cl')
api.add_resource(CategoryTemplate, '/blog/admin/category/template', endpoint='category_template')

api.add_resource(TagRUD, '/blog/admin/tag/<string:key>', endpoint='tag_rud')
api.add_resource(TagCL, '/blog/admin/tag', endpoint='tag_cl')
api.add_resource(TagTemplate, '/blog/admin/tag/template', endpoint='tag_template')

api.add_resource(CommentRUD, '/blog/comment/<string:key>', endpoint='comment_rud')
api.add_resource(CommentC, '/blog/comment', endpoint='comment_c')

api.add_resource(AIMain, '/artificial-intelligence', endpoint='ai_main')
api.add_resource(MusicMain, '/music', endpoint='music_main')
api.add_resource(FitnessMain, '/fitness-and-health', endpoint='fitness_main')
