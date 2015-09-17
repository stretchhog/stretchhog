from google.appengine.ext import ndb


class Category(ndb.Model):
	category = ndb.StringProperty()


class Tag(ndb.Model):
	tag = ndb.StringProperty()
	category = ndb.KeyProperty(kind=Category)


class BlogEntry(ndb.Model):
	title = ndb.StringProperty()
	post = ndb.StringProperty()
	category = ndb.KeyProperty(kind=Category)
	tags = ndb.KeyProperty(kind=Tag, repeated=True)
	user = ndb.UserProperty()
	date_added = ndb.DateTimeProperty(auto_now_add=True)
