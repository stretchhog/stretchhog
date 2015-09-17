from google.appengine.api import users
from google.appengine.ext.ndb.key import Key

from blog.models import Category, Tag, BlogEntry


__author__ = 'tvancann'


def get_by_key(key):
	entity = Key(urlsafe=key)
	return entity.get()


def __to_key(urlsafe):
	return Key(urlsafe=urlsafe)


def __get_all(clazz, *filters):
	qry = clazz.query()
	for f in filters:
		qry = qry.filter(f)
	return qry.fetch()


def create_entry(form):
	entry = BlogEntry(
		title=form.title.data,
		post=form.post.data,
		category=form.category.data,
		tags=form.tags.data,
		user=users.get_current_user)
	return entry.put()


def update_entry_form(form, key):
	entry = get_by_key(key)
	form.title.data = entry.title
	form.title.data = entry.post
	form.category.data = entry.category
	form.category.default = entry.category
	form.tags.data = entry.tags
	form.user.data = entry.user
	return form


def update_entry(key, form):
	entry = get_by_key(key)
	entry.title = form.title.data,
	entry.post = form.post.data,
	entry.category = form.category.data,
	entry.tags = form.tags.data,
	return entry.put()


def delete_entry(key):
	return Key(urlsafe=key).delete()


def get_all_entries():
	return __get_all(BlogEntry)


def create_category(form):
	category = Category(category=form.category.data)
	return category.put()


def update_category_form(form, key):
	category = get_by_key(key)
	form.category.data = category.category
	return form


def update_category(key, form):
	category = get_by_key(key)
	category.category = form.category.data,
	return category.put()


def delete_category(key):
	tags = Tag.query(Tag.category == key).fetch()
	for tag in tags:
		tag.key.delete()
	return Key(urlsafe=key).delete()


def get_all_categories(*filters):
	return __get_all(Category, filters)


def create_tag(form):
	tag = Tag(
		tag=form.tag.data,
		category=__to_key(form.category.data))
	return tag.put()


def update_tag_form(form, key):
	tag = get_by_key(key)
	form.tag.data = tag.tag
	form.category.coerce = str
	form.category.default = tag.category
	return form


def update_tag(key, form):
	tag = get_by_key(key)
	tag.tag = form.tag.data,
	tag.category = form.category.data
	return tag.put()


def delete_tag(key):
	return Key(urlsafe=key).delete()


def get_all_tags(*filters):
	return __get_all(Tag, filters)
