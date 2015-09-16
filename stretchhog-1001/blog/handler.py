from blog.forms import CategoryCreateForm
from blog.models import BlogEntry
from flask import make_response, render_template, request, redirect
from blog import service
from flask.ext.restful import Resource
from main import api

__author__ = 'tvancann'


class BlogEntryCreate(Resource):
	def get(self, id):
		form, tags = service.get_blog_form(id)
		return make_response(render_template('blog/create.html', form=form, tags=tags))

	def post(self):
		service.create_blog(request.get_json())
		return redirect(api.url_for(BlogEntryList), 301)


class BlogEntryDelete(Resource):
	def get(self, id):
		service.delete_blog(id)
		return redirect(api.url_for(BlogEntryList), 301)


class BlogEntryDetail(Resource):
	def get(self, id):
		entry = service.get_by_id(BlogEntry, id)
		return make_response(render_template('blog/detail.html', entry=entry))


class BlogEntryList(Resource):
	def get(self):
		entries = service.get_all_blog()
		return make_response(render_template("blog/list.html", entries=entries))


class CategoryCreate(Resource):
	def get(self):
		return make_response(render_template('blog/category/create.html', form=CategoryCreateForm()))

	def post(self):
		service.create_category(request.get_json())
		return redirect(api.url_for(CategoryCreate), 301)


class TagCreate(Resource):
	def get(self):
		form, categories, tags = service.get_tag_create_form()
		return make_response(render_template('blog/tag/create.html', form=form, categories=categories, tags=tags))

	def post(self):
		service.create_tag(request.get_json())
		return redirect(api.url_for(TagCreate), 301)


class TagEdit(Resource):
	def get(self, id):
		tag = Tag.get_by_id(id)
		form = TagCreateForm()
		form.category.data = tag.category
		form.tag.data = tag.tag

		categories = Category.query().fetch()
		tags = Tag.query().order(Tag.category.category).fetch()
		return make_response(render_template('blog/tag/edit.html', form=form, categories=categories, tags=tags))

	def post(self, id):
		form = TagCreateForm(data=request.get_json())
		category = Category.query(Category.category == form.category.data).fetch()[0]
		tag = Tag.get_by_id(id)
		tag = Tag(
			tag=form.tag.data,
			category=category)
		tag.put()
		return redirect(api.url_for(TagCreate), 301)


class TagDelete(Resource):
	def get(self, id):
		tag = Tag.get_by_id(id)
		tag.key.delete()
		return redirect(api.url_for(TagCreate), 301)


api.add_resource(BlogEntryDelete, '/blog/delete/<int:id>', endpoint='delete_blog_entry')
api.add_resource(BlogEntryDetail, '/blog/<int:id>', endpoint='get_blog_entry')
api.add_resource(BlogEntryList, '/blog', endpoint='list_blog')
# api.add_resource(BlogEntrySearchCategory, '/blog/<int:id>', endpoint='search_blog_category')
# api.add_resource(BlogEntrySearchTag, '/blog/<int:cat_id>/<int:tag_id>', endpoint='search_blog_tag')

api.add_resource(CategoryCreate, '/blog/category/create', endpoint='create_category')
api.add_resource(TagCreate, '/blog/tag/create', endpoint='create_tag')
api.add_resource(TagDelete, '/blog/tag/delete/<int:id>', endpoint='delete_tag')
api.add_resource(TagEdit, '/blog/tag/edit/<int:id>', endpoint='edit_tag')