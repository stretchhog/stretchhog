from google.appengine.ext import ndb
from wtforms.validators import DataRequired


class Category(ndb.Model):
	category = ndb.StringProperty()
	date_added = ndb.DateTimeProperty(auto_now_add=True)


class Tag(ndb.Model):
	tag = ndb.StringProperty()
	date_added = ndb.DateTimeProperty(auto_now_add=True)


class Entry(ndb.Model):
	title = ndb.StringProperty()
	summary = ndb.StringProperty()
	post = ndb.StringProperty()
	tags = ndb.KeyProperty(kind=Tag, repeated=True)
	user = ndb.UserProperty()
	date_added = ndb.DateTimeProperty(auto_now_add=True)


class Comment(ndb.Model):
	email = ndb.StringProperty()
	name = ndb.StringProperty()
	comment = ndb.StringProperty()
	date_added = ndb.DateTimeProperty(auto_now_add=True)
	approved = ndb.BooleanProperty(default=False)
