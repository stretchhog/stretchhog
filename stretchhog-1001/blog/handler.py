from blog.forms import CategoryForm, TagForm, EntryForm
from blog.models import BlogEntry
from flask import make_response, render_template, request, redirect
from blog import service
from blog.view import TagView, CategoryView, EntryView
from flask.ext.restful import Resource
from main import api

__author__ = 'tvancann'


class EntryCreate(Resource):
	def get(self, key):
		form = EntryForm(key)
		return make_response(render_template('blog/entry/create.html', form=form))

	def post(self, key):
		service.create_entry(EntryForm(key, data=request.get_json()))
		return redirect(api.url_for(EntryCreate), 301)


class EntryUpdate(Resource):
	def get(self, key):
		form = EntryForm(key)
		form = service.update_entry_form(form, key)
		return make_response(render_template('blog/entry/create.html', form=EntryForm(key)))

	def post(self, key):
		service.update_entry(key, EntryForm(data=request.get_json()))
		return redirect(api.url_for(EntryCreate), 301)


class EntryDelete(Resource):
	def get(self, key):
		service.delete_entry(key)
		return redirect(api.url_for(EntryCreate), 301)


class EntryDetail(Resource):
	def get(self, key):
		entry = service.get_by_key(key)
		return make_response(render_template('blog/entry/detail.html', entry=entry))


class EntryList(Resource):
	def get(self):
		entries = service.get_all_entries()
		view = [EntryView(entry).__dict__ for entry in entries]
		return view


class CategoryCreate(Resource):
	def get(self):
		form = CategoryForm()
		return make_response(render_template('blog/category/create.html', form=form))

	def post(self):
		service.create_category(CategoryForm(data=request.get_json()))
		return redirect(api.url_for(CategoryCreate), 301)


class CategoryUpdate(Resource):
	def get(self, key):
		form = CategoryForm()
		form = service.update_category_form(form, key)
		return make_response(render_template('blog/category/create.html', form=form))

	def post(self, key):
		service.update_category(key, CategoryForm(data=request.get_json()))
		return redirect(api.url_for(CategoryCreate), 301)


class CategoryDelete(Resource):
	def get(self, key):
		service.delete_category(key)
		return redirect(api.url_for(CategoryCreate), 301)


class CategoryList(Resource):
	def get(self):
		categories = service.get_all_categories()
		view = [CategoryView(cat).__dict__ for cat in categories]
		return view


class TagCreate(Resource):
	def get(self):
		form = TagForm()
		return make_response(render_template('blog/tag/create.html', form=form))

	def post(self):
		service.create_tag(TagForm(data=request.get_json()))
		return redirect(api.url_for(TagCreate), 301)


class TagUpdate(Resource):
	def get(self, key):
		form = TagForm()
		form = service.update_tag_form(form, key)
		return make_response(render_template('blog/tag/create.html', form=form))

	def post(self, key):
		service.update_tag(key, TagForm(data=request.get_json()))
		return redirect(api.url_for(TagCreate), 301)


class TagDelete(Resource):
	def get(self, key):
		service.delete_tag(key)
		return redirect(api.url_for(TagCreate), 301)


class TagList(Resource):
	def get(self):
		tags = service.get_all_tags()
		view = [TagView(tag).__dict__ for tag in tags]
		sorted_view = sorted(view, key=lambda t: t['category'])
		return sorted_view


api.add_resource(EntryCreate, '/blog/admin/entry/create/<string:key>', endpoint='create_entry')
api.add_resource(EntryUpdate, '/blog/admin/entry/update/<string:key>', endpoint='update_entry')
api.add_resource(EntryDelete, '/blog/admin/entry/delete/<string:key>', endpoint='delete_entry')
api.add_resource(EntryDetail, '/blog/entry/<string:key>', endpoint='get_entry')
api.add_resource(EntryList, '/blog/entry/list', endpoint='list_blog')

api.add_resource(CategoryCreate, '/blog/admin/category/create', endpoint='create_category')
api.add_resource(CategoryUpdate, '/blog/admin/category/update/<string:key>', endpoint='update_category')
api.add_resource(CategoryDelete, '/blog/admin/category/delete/<string:key>', endpoint='delete_category')
api.add_resource(CategoryList, '/blog/category/list', endpoint='list_category')

api.add_resource(TagCreate, '/blog/admin/tag/create', endpoint='create_tag')
api.add_resource(TagUpdate, '/blog/admin/tag/update/<string:key>', endpoint='update_tag')
api.add_resource(TagDelete, '/blog/admin/tag/delete/<string:key>', endpoint='delete_tag')
api.add_resource(TagList, '/blog/tag/list', endpoint='list_tag')
