from google.appengine.ext.ndb.key import Key
import time

from blog.forms import CategoryForm, TagForm, EntryForm, CommentForm
from blog.models import Entry, Category, Comment
from flask import make_response, render_template, request, redirect, Response
from blog import service
from blog.view import TagView, CategoryView, EntryView, CommentView
from flask.ext.restful import Resource
from main import api
from flask import Markup, jsonify, json
import markdown


categories = {1: "Music", 2: "Artificial Intelligence", 3: "Fitness & Health"}


class EntryCreate(Resource):
	def get(self, key):
		form = EntryForm(key)
		return make_response(render_template('blog/entry/create.html', form=form))

	def post(self, key):
		service.create_entry(EntryForm(key, data=request.get_json()))
		return redirect(api.url_for(EntryCreate, key=key))


class EntryUpdate(Resource):
	def get(self, key, cat_key):
		form = EntryForm(cat_key)
		form = service.update_entry_form(form, key)
		return make_response(render_template('blog/entry/create.html', form=form))

	def post(self, key, cat_key):
		service.update_entry(key, EntryForm(cat_key, data=request.get_json()))
		return redirect(api.url_for(EntryCreate, key=cat_key))


class EntryDelete(Resource):
	def get(self, key):
		service.delete_entry(key)
		return redirect(api.url_for(EntryCreate, key=key))


class EntryDetail(Resource):
	@staticmethod
	def get_entry(key):
		entry = service.get_by_urlsafe_key(key)
		entry.post = Markup(markdown.markdown(entry.post))
		return entry

	def get(self, key):
		entry = self.get_entry(key)
		comment_form = CommentForm()
		return make_response(render_template('blog/entry/entry.html', entry=entry, form=comment_form))


	def post(self, key):
		comment_form = CommentForm()
		form = CommentForm(data=request.get_json())
		entry = self.get_entry(key)
		if comment_form.validate():
			if request.data['parent_comment']:
				key = request.data['parent_comment']
			service.create_comment(key, form)
		return make_response(render_template('blog/entry/entry.html', entry=entry, form=comment_form))


class EntryList(Resource):
	def get(self):
		entries = service.get_all_entries()
		view = [EntryView(entry) for entry in entries]
		return jsonify(view)


class EntryListCategory(Resource):
	def get(self, cat):
		category = service.get_all_categories(filter=[Category.category == categories[cat]])[0]
		entries = service.get_all_entries_by_ancestor(category.key, sort=[-Entry.date_added])
		view = [EntryView(entry).__dict__ for entry in entries]
		return make_response(render_template("blog/entry/entries.html", entries=view))


class EntrySearch(Resource):
	def post(self):
		entries = service.search(request.data)
		view = [EntryView(entry).__dict__ for entry in entries]
		return view


class CategoryTemplate(Resource):
	def get(self):
		return make_response(render_template('blog/category/list.html'))


class CategoryRUD(Resource):
	def get(self, key):
		entity = service.get_by_urlsafe_key(key)
		view = CategoryView(entity).__dict__
		return Response(json.dumps(view), 201, mimetype='application/json')

	def delete(self, key):
		service.delete_category(key)
		return Response(status=201)

	def put(self, key):
		key = service.update_category(key, CategoryForm(data=request.get_json()))
		view = CategoryView(key.get()).__dict__
		return Response(json.dumps(view), 201, mimetype='application/json')


class CategoryCL(Resource):
	def get(self):
		categories = service.get_all_categories()
		view = [CategoryView(cat).__dict__ for cat in categories]
		return Response(json.dumps(view), 200, mimetype='application/json')

	def post(self):
		form = CategoryForm(data=request.get_json())
		if form.validate():
			key = service.create_category(form)
			view = CategoryView(key.get()).__dict__
			return Response(json.dumps(view), 201, mimetype='application/json')
		else:
			return Response(status=400, mimetype='application/json')




class TagCreate(Resource):
	def get(self):
		form = TagForm()
		return make_response(render_template('blog/tag/create.html', form=form))

	def post(self):
		service.create_tag(TagForm(data=request.get_json()))
		return redirect(api.url_for(TagCreate))


class TagUpdate(Resource):
	def get(self, key):
		form = TagForm()
		form = service.update_tag_form(form, key)
		return make_response(render_template('blog/tag/create.html', form=form))

	def post(self, key):
		service.update_tag(key, TagForm(data=request.get_json()))
		return redirect(api.url_for(TagCreate))


class TagDelete(Resource):
	def get(self, key):
		service.delete_tag(key)
		return redirect(api.url_for(TagCreate))


class TagList(Resource):
	def get(self):
		tags = service.get_all_tags()
		view = [TagView(tag).__dict__ for tag in tags]
		sorted_view = sorted(view, key=lambda t: t['category'])
		return sorted_view


class CommentList(Resource):
	def get(self, key):
		comments = service.get_all_comments_by_ancestor(Key(urlsafe=key), sort=[-Comment.date_added])
		view = [CommentView(comment).__dict__ for comment in comments]
		return view


api.add_resource(EntryCreate, '/blog/admin/entry/create/<string:key>', endpoint='create_entry')
api.add_resource(EntryUpdate, '/blog/admin/entry/update/<string:key>/<string:cat_key>', endpoint='update_entry')
api.add_resource(EntryDelete, '/blog/admin/entry/delete/<string:key>', endpoint='delete_entry')
api.add_resource(EntryDetail, '/blog/entry/<string:key>', endpoint='get_entry')
api.add_resource(EntryList, '/blog/entry/list', endpoint='list_entry')
api.add_resource(EntryListCategory, '/blog/entry/list/<int:cat>', endpoint='category_entry')
api.add_resource(EntrySearch, '/blog/entry/search', endpoint='search_entry')

api.add_resource(CommentList, '/blog/comment/list/<string:key>', endpoint='list_comment')

api.add_resource(CategoryRUD, '/blog/admin/category/<string:key>', endpoint='category_rud')
api.add_resource(CategoryCL, '/blog/admin/category', endpoint='category_cl')
api.add_resource(CategoryTemplate, '/blog/admin/category/template', endpoint='category_template')

api.add_resource(TagCreate, '/blog/admin/tag/create', endpoint='create_tag')
api.add_resource(TagUpdate, '/blog/admin/tag/update/<string:key>', endpoint='update_tag')
api.add_resource(TagDelete, '/blog/admin/tag/delete/<string:key>', endpoint='delete_tag')
api.add_resource(TagList, '/blog/tag/list', endpoint='list_tag')
