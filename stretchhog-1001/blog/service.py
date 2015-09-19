from google.appengine.api import users
from google.appengine.ext.ndb.key import Key

from blog.models import Category, Tag, BlogEntry


def get_by_key(key):
	entity = Key(urlsafe=key)
	return entity.get()


def __to_key(urlsafe):
	return Key(urlsafe=urlsafe)


def __get_all(clazz, **kwargs):
	qry = clazz.query()
	if 'filter' in kwargs:
		for f in kwargs['filter']:
			qry = qry.filter(f)
	if 'sort' in kwargs:
		for s in kwargs['sort']:
			qry.order(s)
	return qry.fetch()


def create_entry(form):
	entry = BlogEntry()
	entry.title = form.title.data
	entry.summary = form.summary.data
	entry.post = form.post.data
	entry.category = Key(urlsafe=form.category.data)
	entry.tags = [Key(urlsafe=tag) for tag in form.tags.data]
	entry.user = users.get_current_user()
	return entry.put()


def update_entry_form(form, key):
	entry = get_by_key(key)
	form.tags.data = [tag.urlsafe() for tag in entry.tags]
	form.title.data = entry.title
	form.summary.data = entry.summary
	form.post.data = entry.post
	return form


def update_entry(key, form):
	entry = get_by_key(key)
	entry.title = form.title.data
	entry.summary = form.summary.data
	entry.post = form.post.data
	entry.tags = [Key(urlsafe=tag) for tag in form.tags.data]
	return entry.put()


def delete_entry(key):
	return Key(urlsafe=key).delete()


def get_all_entries(**kwargs):
	return __get_all(BlogEntry, **kwargs)


def create_category(form):
	category = Category(category=form.category.data)
	return category.put()


def update_category_form(form, key):
	category = get_by_key(key)
	form.category.data = category.category
	return form


def update_category(key, form):
	category = get_by_key(key)
	category.category = form.category.data
	return category.put()


def delete_category(key):
	tags = Tag.query(Tag.category == Key(urlsafe=key)).fetch()
	for tag in tags:
		tag.key.delete()
	return Key(urlsafe=key).delete()


def get_all_categories(**kwargs):
	return __get_all(Category, **kwargs)


def create_tag(form):
	tag = Tag(
		tag=form.tag.data,
		category=__to_key(form.category.data))
	return tag.put()


def update_tag_form(form, key):
	tag = get_by_key(key)
	form.category.data = tag.category.urlsafe()
	form.tag.data = tag.tag
	return form


def update_tag(key, form):
	tag = get_by_key(key)
	tag.tag = form.tag.data
	tag.category = Key(urlsafe=form.category.data)
	return tag.put()


def delete_tag(key):
	return Key(urlsafe=key).delete()


def get_all_tags(**kwargs):
	return __get_all(Tag, **kwargs)


def search(data):
	qry = BlogEntry.query()
	if 'category' in data:
		qry.filter(BlogEntry.category == Key(urlsafe=data['category']))
	if 'tag' in data:
		qry.filter(BlogEntry.tags == Key(urlsafe=data['tag']))
	return qry.fetch()
