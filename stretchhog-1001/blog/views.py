import urllib, hashlib
from blog.models import Comment
from main import markdown

__author__ = 'tvancann'

from blog import service


class TagView:
	def __init__(self, entity):
		self.key = entity.key.urlsafe()
		self.tag = entity.tag
		self.category = CategoryView(entity.key.parent().get()).__dict__


class CategoryView:
	def __init__(self, entity):
		self.key = entity.key.urlsafe()
		self.category = entity.category


class EntryView:
	@staticmethod
	def get_comments(entity):
		return service.get_all_comments_by_ancestor(entity.key, sort=[-Comment.date_added])

	def __init__(self, entity):
		self.key = entity.key.urlsafe()
		self.title = entity.title
		self.summary = entity.summary
		self.post = entity.post
		self.category = CategoryView(entity.key.parent().get()).__dict__
		self.tags = [TagView(tag.get()).__dict__ for tag in entity.tags]
		self.date_added = entity.date_added.isoformat()
		sorted_comments = sorted(self.get_comments(entity), key=lambda c: c.date_added, reverse=True)
		self.comments = [CommentView(comment).__dict__ for comment in sorted_comments]
		self.comment_count = sum(comment['approved'] is True for comment in self.comments)


class EntryPostView:
	def __init__(self, entity):
		self.post = markdown(entity.post)


class CommentView:
	def __init__(self, entity):
		self.key = entity.key.urlsafe()
		self.parentKey = entity.key.parent().urlsafe()
		self.comment = entity.comment
		self.date_added = entity.date_added.isoformat()
		self.name = entity.name
		self.approved = entity.approved
		self.spam = entity.spam

		# Set your variables here
		self.email = entity.email
		size = 80
		# construct the url
		gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(self.email.lower()).hexdigest() + "?"
		gravatar_url += urllib.urlencode({'d': 'mm', 's': str(size)})
		self.image = gravatar_url
