from google.appengine.api import users
from google.appengine.ext.ndb.key import Key
from blog.models import Category, Tag, Entry, Comment


def get_by_urlsafe_key(key):
	entity = Key(urlsafe=key)
	return entity.get()


def to_key(urlsafe):
	return Key(urlsafe=urlsafe)


def __get_all(qry, **kwargs):
	if 'filter' in kwargs:
		for f in kwargs['filter']:
			qry = qry.filter(f)
	if 'sort' in kwargs:
		for s in kwargs['sort']:
			qry.order(s)
	return qry.fetch()


def create_entry(form):
	entry = Entry(parent=to_key(form.category.data))
	entry.title = form.title.data
	entry.summary = form.summary.data
	entry.post = form.post.data
	entry.tags = [Key(urlsafe=tag) for tag in form.tags.data]
	entry.user = users.get_current_user()
	return entry.put()


def update_entry_form(form, key):
	entry = get_by_urlsafe_key(key)
	form.tags.data = [tag.urlsafe() for tag in entry.tags]
	form.title.data = entry.title
	form.summary.data = entry.summary
	form.post.data = entry.post
	return form


def update_entry(key, form):
	entry = get_by_urlsafe_key(key)
	entry.title = form.title.data
	entry.summary = form.summary.data
	entry.post = form.post.data
	entry.tags = [Key(urlsafe=tag) for tag in form.tags.data]
	return entry.put()


def delete_entry(key):
	return Key(urlsafe=key).delete()


def get_all_entries(**kwargs):
	return __get_all(Entry.query(), **kwargs)


def create_category(form):
	category = Category(category=form.category.data)
	return category.put()


def update_category_form(form, key):
	category = get_by_urlsafe_key(key)
	form.category.data = category.category
	return form


def update_category(key, form):
	category = get_by_urlsafe_key(key)
	category.category = form.category.data
	return category.put()


def delete_category(key):
	tags = Tag.query(ancestor=Key(urlsafe=key)).fetch()
	for tag in tags:
		tag.key.delete()
	return Key(urlsafe=key).delete()


def get_all_categories(**kwargs):
	return __get_all(Category.query(), **kwargs)


def create_tag(form):
	tag = Tag(
		parent=to_key(form.category.data),
		tag=form.tag.data)
	return tag.put()


def update_tag(key, form):
	tag = get_by_urlsafe_key(key)
	tag.tag = form.tag.data
	return tag.put()


def delete_tag(key):
	return Key(urlsafe=key).delete()


def get_all_tags(**kwargs):
	return __get_all(Tag.query(), **kwargs)


def search(data):
	qry = Entry.query()
	if 'category' in data:
		qry.filter(Entry.category == Key(urlsafe=data['category']))
	if 'tag' in data:
		qry.filter(Entry.tags == Key(urlsafe=data['tag']))
	return qry.fetch()


def create_comment(form):
	comment = Comment(parent=to_key(form.parent.data),
	                  user=users.get_current_user(),
	                  comment=form.comment.data)
	return comment.put()


def update_comment(key, form):
	comment = get_by_urlsafe_key(key)
	comment.approved = True
	return comment.put()


def get_all_comments(**kwargs):
	return __get_all(Comment, **kwargs)


def get_all_tags_by_ancestor(ancestor):
	return __get_all(Tag.query(ancestor=ancestor))


def get_all_entries_by_ancestor(ancestor, **kwargs):
	return __get_all(Entry.query(ancestor=ancestor), **kwargs)


def get_all_comments_by_ancestor(ancestor, **kwargs):
	return __get_all(Comment.query(ancestor=ancestor), **kwargs)


def count_comments_by_ancestor(ancestor):
	return Comment.query(ancestor=ancestor).count()
