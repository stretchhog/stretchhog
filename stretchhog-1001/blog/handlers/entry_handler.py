import json

from blog.forms import EntryForm
from blog.handlers.handler import Handler, blog_api_root, admin_blog_root
from blog.models import Entry, Category, Tag
from blog.services.entry_service import service
from blog.views import EntryView, EntryAdminView, EntrySummaryView, EntryBannerView
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


class EntryBannerInfo(Resource):
	def get(self, year, month, slug):
		entry = service.get_by_slug(Entry, slug)
		view = EntryBannerView(entry).__dict__
		return Response(json.dumps(view), 200, mimetype='application/json')


class EntryList(Resource):
	def get(self):
		entries = service.get_all_entries()
		return get_sorted_entries_response_by_date(entries)


entry = '/entry'
api.add_resource(EntryRUD, admin_blog_root + entry + '/<string:key>', endpoint='entry_rud')
api.add_resource(EntryCL, admin_blog_root + entry, endpoint='entry_cl')

api.add_resource(EntryByCategory, blog_api_root + entry + '/category/<string:category>', endpoint='entry_category')
api.add_resource(EntryByYear, blog_api_root + entry + '/year/<int:year>', endpoint='entry_year')
api.add_resource(EntryByMonth, blog_api_root + entry + '/month/<int:year>/<int:month>', endpoint='entry_month')
api.add_resource(EntryBySlug, blog_api_root + entry + '/slug/<int:year>/<int:month>/<string:slug>', endpoint='entry_slug')
api.add_resource(EntryList, blog_api_root + entry + '/list', endpoint='entry_list')
api.add_resource(EntryByTag, blog_api_root + entry + '/tag/<string:tag>', endpoint='entry_tag')

api.add_resource(EntryBannerInfo, blog_api_root + entry + '/banner/<int:year>/<int:month>/<string:slug>')
