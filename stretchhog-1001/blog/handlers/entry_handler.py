import json

from flask import Response, request
from entry_service import service
from flask.ext.restful import Resource
from forms import EntryForm
from handler import Handler
from main import api
from views import EntryView, EntryAdminView


class EntryHandler(Handler):
	def __init__(self, comment_service, form, view):
		super(EntryHandler, self).__init__(comment_service, form, view)


handler = EntryHandler(service, EntryForm, EntryAdminView)


class EntryRUD(Resource):
	@staticmethod
	def get(self, key):
		entry = service.get_by_urlsafe_key(key)
		view = EntryView(entry).__dict__
		return Response(view, 200, mimetype='application/json')

	@staticmethod
	def put(self, key):
		return handler.put_response_for(key, request)

	@staticmethod
	def delete(self, key):
		return handler.delete_response_for(key)


class EntryCL(Resource):
	@staticmethod
	def get(self):
		entries = service.get_all_entries()
		return get_sorted_entries_response_by_date(entries)

	@staticmethod
	def post(self):
		return handler.post_response_for(request)


class EntryPost(Resource):
	@staticmethod
	def get(self, key):
		entry = service.get_by_urlsafe_key(key)
		view = EntryAdminView(entry).__dict__
		return Response(json.dumps(view), 200, mimetype='application/json')


def get_sorted_entries_response_by_date(entries):
	sorted_entries = sorted(entries, key=lambda e: e.created, reverse=True)
	view = [EntryView(entry).__dict__ for entry in sorted_entries]
	return Response(json.dumps(view), 200, mimetype='application/json')


class EntryByYear(Resource):
	def get(self, year):
		entries = service.get_all_entries_by_year(year)
		return get_sorted_entries_response_by_date(entries)


class EntryByMonth(Resource):
	def get(self, year, month):
		entries = service.get_all_entries_by_month(year, month)
		return get_sorted_entries_response_by_date(entries)


class EntryBySlug(Resource):
	def get(self, year, month, slug):
		entry = service.get_entry_by_slug(slug)
		view = EntryView(entry).__dict__
		return Response(view, 200, mimetype='application/json')


api.add_resource(EntryRUD, '/blog/admin/entry/<string:key>', endpoint='entry_rud')
api.add_resource(EntryCL, '/blog/admin/entry', endpoint='entry_cl')

api.add_resource(EntryByYear, '/blog/<string:year>')
api.add_resource(EntryByMonth, '/blog/<string:year>/<string:month>')
api.add_resource(EntryBySlug, '/blog/<string:year>/<string:month>/<string:slug>')
