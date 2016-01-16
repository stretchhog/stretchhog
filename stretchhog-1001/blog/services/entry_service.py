from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.ext.ndb.key import Key
from blog.models import Entry
from service import Service
import datetime


class EntryService(Service):
	def __init__(self):
		super(EntryService, self).__init__()

	def create(self, form):
		entry = Entry(parent=Service.to_key(form.category.data))
		entry.title = form.title.data
		entry.summary = form.summary.data
		entry.post = form.post.data
		entry.tags = [Key(urlsafe=tag) for tag in form.tags.data]
		entry.slug = Service.slugify(entry.title)
		# entry.user = users.get_current_user()
		return entry.put()

	def update(self, key, form):
		entry = Service.get_by_urlsafe_key(key)
		if entry.title is not form.title.data:
			entry.slug = Service.slugify(entry.title)
			entry.title = form.title.data
		entry.summary = form.summary.data
		entry.post = form.post.data
		entry.tags = [Key(urlsafe=tag) for tag in form.tags.data]
		return entry.put()

	def get(self, key):
		return Key(urlsafe=key).delete()

	def delete(self, key):
		return Key(urlsafe=key).delete()

	@staticmethod
	def get_all_entries(**kwargs):
		return Service.get_all(Entry.query(), **kwargs)

	@staticmethod
	def get_all_entries_by_ancestor(ancestor, **kwargs):
		return Service.get_all(Entry.query(ancestor=ancestor), **kwargs)

	@staticmethod
	def get_all_entries_by_year(year, **kwargs):
		return Service.get_all(Entry.query(ndb.AND(Entry.created > datetime.datetime(year, 1, 1, 0, 0),
		                                           Entry.created < datetime.datetime(year + 1, 1, 1, 0, 0))), **kwargs)

	@staticmethod
	def get_all_entries_by_month(year, month, **kwargs):
		return Service.get_all(Entry.query(ndb.AND(Entry.created > datetime.datetime(year, month, 1, 1, 0, 0),
		                                           Entry.created < datetime.datetime(year, month + 1, 1, 0, 0))), **kwargs)

	@staticmethod
	def get_entry_by_slug(slug):
		return Service.get_all(Entry.query(Entry.slug == slug))[0]

	@staticmethod
	def get_all_entries_by_repeated_property(property, search, **kwargs):
		return Service.get_all(Entry.query(property == search.key), **kwargs)

service = EntryService()
