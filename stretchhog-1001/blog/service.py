from google.appengine.api import users
from google.appengine.ext.ndb.key import Key

from blog.models import Category, Tag, BlogEntry


__author__ = 'tvancann'


def get_by_key(key):
	entity = Key(urlsafe=key)
	return entity.get()


def __to_key(urlsafe):
	return Key(urlsafe=urlsafe)


def __get_all(clazz):
	return clazz.query().fetch()


def get_all_categories():
	return __get_all(Category)


def get_blog_form(id):
	category = get_by_key(id)
	tags = Tag.query(Category.category == category).fetch()
	form = BlogEntryCreateForm()
	form.category.data = category
	form.tags.choices = [(tag.key.urlsafe(), tag.tag) for tag in tags]
	return form, tags


def create_blog(data):
	form = BlogEntryCreateForm(data=data)
	category = get_by_key(form.category.data)
	entry = BlogEntry(
		title=form.title.data,
		post=form.post.data,
		category=category,
		tags=form.tags.data,
		user=users.get_current_user)
	return entry.put()


def delete_blog(id):
	return get_by_key(id).key.delete()


def create_category(form):
	category = Category(category=form.category.data)
	return category.put()

def update_category(key, form):
	category = get_by_key(key)
	category.category = form.category.data,
	return category.put()

def delete_category(key):
	tags = Tag.query(Tag.category == key).fetch()
	for tag in tags:
		tag.key.delete()
	return Key(urlsafe=key).delete()

def create_tag(form):
	tag = Tag(
		tag=form.tag.data,
		category=__to_key(form.category.data))
	return tag.put()


def update_tag_form(form, key):
	tag = get_by_key(key)
	form.tag.data = tag.tag
	form.category.coerce = str
	form.category.default = Category.query(Category.category == tag.category.category).fetch()[0].key.urlsafe()
	return form


def update_tag(key, form):
	tag = get_by_key(key)
	tag.tag = form.tag.data,
	tag.category = form.category.data
	return tag.put()


def delete_tag(key):
	return Key(urlsafe=key).delete()


def get_all_tags():
	return __get_all(Tag)


def update_category_form(form, key):
	category = get_by_key(key)
	form.category.data = category.category
	return form
