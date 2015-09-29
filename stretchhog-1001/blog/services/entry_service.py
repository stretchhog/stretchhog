from google.appengine.ext import ndb
from google.appengine.ext.ndb.key import Key

from blog.models import Entry
from service import Service


class EntryService(Service):
	def __init__(self):
		super(EntryService, self).__init__()

	def create(self, form):
		entry = Entry(parent=Service.to_key(form.category.data))
		entry.title = form.title.data
		entry.summary = form.summary.data
		entry.post = form.post.data
		entry.tags = [Key(urlsafe=tag) for tag in form.tags.data]
		return entry.put()

	def update(self, key, form):
		entry = Service.get_by_urlsafe_key(key)
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
	def get_all_entries_by_year(year):
		return Service.get_all(Entry.query(Entry.created.year == year))

	@staticmethod
	def get_all_entries_by_month(year, month):
		return Service.get_all(Entry.query(ndb.AND(Entry.created.year == year, Entry.created.month == month)))

	@staticmethod
	def get_entry_by_slug(slug):
		return Service.get_all(Entry.query(Entry.slug == slug))


service = EntryService()
