from google.appengine.ext.ndb.key import Key

from blog.models import Tag
from service import Service


class TagService(Service):
	def __init__(self):
		super(TagService, self).__init__()

	def create(self, form):
		tag = Tag(
			parent=Service.to_key(form.category.data),
			tag=form.tag.data)
		return tag.put()

	def update(self, key, form):
		tag = Service.get_by_urlsafe_key(key)
		tag.tag = form.tag.data
		return tag.put()

	def get(self, key):
		return Key(urlsafe=key).delete()

	def delete(self, key):
		tags = Tag.query(ancestor=Key(urlsafe=key)).fetch()
		for tag in tags:
			tag.key.delete()
		return Key(urlsafe=key).delete()

	@staticmethod
	def get_all_tags(**kwargs):
		return Service.get_all(Tag.query(), **kwargs)

	@staticmethod
	def get_all_tags_by_ancestor(ancestor):
		return Service.get_all(Tag.query(ancestor=ancestor))


service = TagService()
