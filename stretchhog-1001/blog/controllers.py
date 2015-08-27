from flask import render_template, make_response, redirect
from flask.ext.restful import Resource
from blog.models import BlogEntry
from main import api


class BlogEntryDelete(Resource):
	def get(self, id):
		BlogEntry.get_by_id(id).key.delete()
		return redirect(api.url_for(BlogEntryList), 301)


class BlogEntryDetail(Resource):
	def get(self, id):
		comic = BlogEntry.get_by_id(id)
		return make_response(render_template('blog/detail.html', comic=comic))


class BlogEntryList(Resource):
	def get(self, category, tags):
		result = BlogEntry.query().fetch()
		return make_response(render_template("blog/list.html", entries=result))


class BlogEntrySearchCategory(Resource):
	def get(self, category):
		pass

	def post(self):
		pass


class BlogEntrySearchTag(Resource):
	def get(self, category, tag):
		qry = BlogEntry.query()
		if category:
			qry.filter(BlogEntry.category.category == category)
		if tag:
			qry.filter(BlogEntry.tags.tag == tag)
		result = qry.fetch()
		return make_response(render_template("blog/list.html", entries=result))

	def post(self):
		pass


api.add_resource(BlogEntryDelete, '/blog/delete/<int:id>', endpoint='delete_blog_entry')
api.add_resource(BlogEntryDetail, '/blog/<int:id>', endpoint='get_blog_entry')
api.add_resource(BlogEntryList, '/blog', endpoint='list_blog')
api.add_resource(BlogEntrySearchCategory, '/blog/<int:id>', endpoint='search_blog_category')
api.add_resource(BlogEntrySearchTag, '/blog/<int:id>/<int:id>', endpoint='search_blog_tag')
