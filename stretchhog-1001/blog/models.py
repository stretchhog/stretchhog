from google.appengine.ext import ndb


class Category(ndb.Model):
	category = ndb.StringProperty()
	slug = ndb.StringProperty()
	created = ndb.DateTimeProperty(auto_now_add=True)


class Tag(ndb.Model):
	tag = ndb.StringProperty()
	created = ndb.DateTimeProperty(auto_now_add=True)


class Entry(ndb.Model):
	title = ndb.StringProperty()
	summary = ndb.StringProperty()
	post = ndb.StringProperty()
	tags = ndb.KeyProperty(kind=Tag, repeated=True)
	user = ndb.UserProperty()
	created = ndb.DateTimeProperty(auto_now_add=True)
	slug = ndb.StringProperty()
	# stats
	views = ndb.IntegerProperty(default=0)
	likes = ndb.IntegerProperty(default=0)
	shares = ndb.IntegerProperty(default=0)


class Comment(ndb.Model):
	email = ndb.StringProperty()
	name = ndb.StringProperty()
	comment = ndb.StringProperty()
	created = ndb.DateTimeProperty(auto_now_add=True)
	# These two boolean fields are mutually exclusive, only one can be True
	approved = ndb.BooleanProperty(default=False)
	spam = ndb.BooleanProperty(default=False)
