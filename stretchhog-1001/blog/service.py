from google.appengine.api import users

from blog.forms import BlogEntryCreateForm, CategoryCreateForm, TagCreateForm
from blog.models import Category, Tag, BlogEntry


__author__ = 'tvancann'


def __get_by_id(clazz, id):
	return clazz.get_by_id(id)


def __get_all(clazz):
	return clazz.query().fetch()


def get_blog_form(id):
	category = __get_by_id(Category, id)
	tags = Tag.query(Category.category == category).fetch()
	form = BlogEntryCreateForm()
	form.category.data = category
	return form, tags


def create_blog(data):
	form = BlogEntryCreateForm(data=data)
	entry = BlogEntry(
		title=form.title.data,
		post=form.post.data,
		category=form.category.data,
		tags=form.tags.data,
		user=users.get_current_user)
	return entry.put()


def delete_blog(id):
	return __get_by_id(BlogEntry, id).key.delete()


def get_blog_by_id(id):
	return __get_by_id(BlogEntry, id)


def get_all_blog():
	return __get_all(BlogEntry)


def create_category(data):
	form = CategoryCreateForm(data=data)
	category = Category(category=form.category.data)
	return category.put()


def get_all_categories():
	"""
	:rtype: Category
	"""
	return __get_all(Category)


def create_tag(data):
	form = TagCreateForm(data=data)
	category = Category.query(Category.category == form.category.data).fetch()[0]
	tag = Tag(
		tag=form.tag.data,
		category=category)
	return tag.put()

def get_tag_create_form():
	categories = get_all_categories()
	tags = Tag.query().order(Tag.category.category).fetch()
	form = TagCreateForm()
	return form, categories, tags
