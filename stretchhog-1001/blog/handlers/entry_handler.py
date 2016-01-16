import json

from blog.forms import EntryForm
from blog.handlers.handler import Handler, root_blog_api
from blog.models import Entry, Category, Tag
from blog.services.entry_service import service
from blog.views import EntryView, EntryAdminView, EntrySummaryView
from flask import Response, request
from flask.ext.restful import Resource
from main import api


class EntryHandler(Handler):
	def __init__(self, comment_service, form, view):
		super(EntryHandler, self).__init__(comment_service, form, view)


handler = EntryHandler(service, EntryForm, EntryAdminView)


class EntryRUD(Resource):
	@staticmethod
	def get(key):
		return handler.get_response_for(urlsafe=key)

	@staticmethod
	def put(key):
		return handler.put_response_for(key, request)

	@staticmethod
	def delete(key):
		return handler.delete_response_for(key)


class EntryCL(Resource):
	@staticmethod
	def get():
		entries = service.get_all_entries(sort=[-Entry.created])
		view = [EntryAdminView(entry).__dict__ for entry in entries]
		return Response(json.dumps(view), 200, mimetype='application/json')

	@staticmethod
	def post():
		return handler.post_response_for(request)


class EntryByCategory(Resource):
	@staticmethod
	def get(category):
		category_entity = service.get_by_slug(Category, category)
		if category_entity is not None:
			entries = service.get_all_entries_by_ancestor(category_entity.key, sort=[-Entry.created])
		else:
			entries = []
		return get_sorted_entries_response_by_date(entries)


class EntryByTag(Resource):
	@staticmethod
	def get(tag):
		tag_entity = service.get_by_slug(Tag, tag)
		if tag_entity is not None:
			entries = service.get_all_entries_by_repeated_property(Entry.tags, tag_entity, sort=[-Entry.created])
		else:
			entries = []
		return get_sorted_entries_response_by_date(entries)


def get_sorted_entries_response_by_date(entries):
	view = [EntrySummaryView(e).__dict__ for e in entries]
	return Response(json.dumps(view), 200, mimetype='application/json')


class EntryByYear(Resource):
	@staticmethod
	def get(year):
		entries = service.get_all_entries_by_year(year, sort=[-Entry.created])
		return get_sorted_entries_response_by_date(entries)


class EntryByMonth(Resource):
	def get(self, year, month):
		entries = service.get_all_entries_by_month(year, month, sort=[-Entry.created])
		return get_sorted_entries_response_by_date(entries)


class EntryBySlug(Resource):
	def get(self, year, month, slug):
		entry = service.get_by_slug(Entry, slug)
		view = EntryView(entry).__dict__
		return Response(json.dumps(view), 200, mimetype='application/json')


class EntryList(Resource):
	def get(self):
		entries = service.get_all_entries()
		return get_sorted_entries_response_by_date(entries)


entry = '/entry'
api.add_resource(EntryRUD, root_blog_api + entry + '/<string:key>', endpoint='entry_rud')
api.add_resource(EntryCL, root_blog_api + entry, endpoint='entry_cl')

api.add_resource(EntryByCategory, root_blog_api + entry + '/category/<string:category>', endpoint='entry_category')
api.add_resource(EntryByYear, root_blog_api + entry + '/year/<int:year>', endpoint='entry_year')
api.add_resource(EntryByMonth, root_blog_api + entry + '/month/<int:year>/<int:month>', endpoint='entry_month')
api.add_resource(EntryBySlug, root_blog_api + entry + '/slug/<int:year>/<int:month>/<string:slug>', endpoint='entry_slug')
api.add_resource(EntryList, root_blog_api + entry + '/list', endpoint='entry_list')
api.add_resource(EntryByTag, root_blog_api + entry + '/tag/<string:tag>', endpoint='entry_tag')
