from google.appengine.ext import ndb


class Category(ndb.Model):
	category = ndb.StringProperty()


class Tag(ndb.Model):
	tag = ndb.StringProperty()
	category = ndb.StructuredProperty(Category, repeated=False)


class BlogEntry(ndb.Model):
	title = ndb.IntegerProperty()
	post = ndb.StringProperty()
	category = ndb.StructuredProperty(Category, repeated=False)
	tags = ndb.StructuredProperty(Tag, repeated=True)
	user = ndb.UserProperty()
	date_added = ndb.DateTimeProperty(auto_now_add=True)
