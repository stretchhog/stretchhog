from blog.forms import CategoryForm, TagForm
from blog.models import BlogEntry
from flask import make_response, render_template, request, redirect, jsonify
from blog import service
from blog.view import TagView
from flask.ext.restful import Resource
from main import api

__author__ = 'tvancann'


class BlogEntryCreate(Resource):
	def get(self, key):
		form, tags = service.get_blog_form(key)
		return make_response(render_template('blog/create.html', form=form, tags=tags))

	def post(self):
		service.create_blog(request.get_json())
		return redirect(api.url_for(BlogEntryList), 301)


class BlogEntryDelete(Resource):
	def get(self, key):
		service.delete_blog(key)
		return redirect(api.url_for(BlogEntryList), 301)


class BlogEntryDetail(Resource):
	def get(self, key):
		entry = service.get_by_id(BlogEntry, key)
		return make_response(render_template('blog/detail.html', entry=entry))


class BlogEntryList(Resource):
	def get(self):
		entries = service.get_all_blog()
		return make_response(render_template("blog/list.html", entries=entries))


class CategoryCreate(Resource):
	def get(self):
		form = CategoryForm()
		return make_response(render_template('blog/category/create.html', form=form))

	def post(self):
		service.create_category(CategoryForm(data=request.get_json()))
		return redirect(api.url_for(CategoryCreate), 301)


class TagCreate(Resource):
	def get(self):
		form = TagForm()
		return make_response(render_template('blog/tag/create.html', form=form))

	def post(self):
		service.create_tag(TagForm(data=request.get_json()))
		return redirect(api.url_for(TagCreate), 301)

class TagList(Resource):
	def get(self):
		tags = service.get_all_tags()
		view = [TagView(tag).__dict__ for tag in tags]
		sorted_view = sorted(view, key=lambda t: t['category'])
		return sorted_view


class TagUpdate(Resource):
	def get(self, key):
		form = TagForm()
		form = service.update_tag_form(form, key)
		return make_response(render_template('blog/tag/edit.html', form=form))

	def post(self, key):
		service.update_tag(key, TagForm(data=request.get_json()))
		return redirect(api.url_for(TagCreate), 301)


class TagDelete(Resource):
	def get(self, key):
		service.delete_tag(key)
		return redirect(api.url_for(TagCreate), 301)


api.add_resource(BlogEntryDelete, '/blog/delete/<string:key>', endpoint='delete_blog_entry')
api.add_resource(BlogEntryDetail, '/blog/<string:key>', endpoint='get_blog_entry')
api.add_resource(BlogEntryList, '/blog', endpoint='list_blog')

api.add_resource(CategoryCreate, '/blog/category/create', endpoint='create_category')

api.add_resource(TagCreate, '/blog/tag/create', endpoint='create_tag')
api.add_resource(TagUpdate, '/blog/tag/update/<string:key>', endpoint='update_tag')
api.add_resource(TagDelete, '/blog/tag/delete/<string:key>', endpoint='delete_tag')
api.add_resource(TagList, '/blog/tag/list', endpoint='list_tag')
