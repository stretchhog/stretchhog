from google.appengine.ext.ndb.key import Key

from blog.models import Comment, Tag
from service import Service


class CommentService(Service):
	def __init__(self):
		super(CommentService, self).__init__()

	def create(self, form):
		comment = Comment(parent=Service.to_key(form.parent.data),
		                  email=form.email.data,
		                  name=form.name.data,
		                  comment=form.comment.data)
		return comment.put()

	def update(self, key, form):
		pass

	def get(self, key):
		return Service.get_by_urlsafe_key(key)

	def delete(self, key):
		return Key(urlsafe=key).delete()

	@staticmethod
	def approve_comment(key):
		comment = Service.get_by_urlsafe_key(key)
		comment.approved = True
		return comment.put()

	@staticmethod
	def spam_comment(key):
		comment = Service.get_by_urlsafe_key(key)
		comment.spam = True
		return comment.put

	@staticmethod
	def get_all_comments(**kwargs):
		return Service.get_all(Comment, **kwargs)

	@staticmethod
	def get_all_comments_by_ancestor(ancestor, **kwargs):
		return Service.get_all(Comment.query(ancestor=ancestor), **kwargs)

	@staticmethod
	def count_comments_by_ancestor(ancestor):
		return Comment.query(ancestor=ancestor).filter(Comment.approved == True).count()


service = CommentService()
