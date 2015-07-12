from google.appengine.ext import ndb


class Comic(ndb.Model):
	number = ndb.IntegerProperty()
	title = ndb.StringProperty()
	notes = ndb.StringProperty()
	image = ndb.BlobProperty()
	date_added = ndb.DateTimeProperty(auto_now_add=True)

class User(ndb.Model):
	pass
