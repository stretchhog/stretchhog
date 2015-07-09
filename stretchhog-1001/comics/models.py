from google.appengine.ext import ndb


class Comic(ndb.Model):
	number = ndb.IntegerProperty()
	title = ndb.StringProperty()
	notes = ndb.StringProperty()
	date_added = ndb.DateTimeProperty(auto_now_add=True)

	@classmethod
	def query_comic(cls, ancestor_key):
		return cls.query(ancestor=ancestor_key).order(cls.number)
