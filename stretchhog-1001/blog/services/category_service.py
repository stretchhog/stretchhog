from google.appengine.ext.ndb.key import Key

from blog.models import Category, Tag
from blog.services.service import Service


class CategoryService(Service):
	def __init__(self):
		super(CategoryService, self).__init__()

	def create(self, form):
		category = Category(category=form.category.data)
		return category.put()

	def update(self, key, form):
		category = Service.get_by_urlsafe_key(key)
		category.category = form.category.data
		return category.put()

	def get(self, key):
		return Service.get_by_urlsafe_key(key)

	def delete(self, key):
		tags = Tag.query(ancestor=Key(urlsafe=key)).fetch()
		for tag in tags:
			tag.key.delete()
		return Key(urlsafe=key).delete()

	@staticmethod
	def get_all_categories(**kwargs):
		return Service.get_all(Category.query(), **kwargs)


service = CategoryService()
