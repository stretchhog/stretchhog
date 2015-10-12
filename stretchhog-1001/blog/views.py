import hashlib
import urllib

from google.appengine.ext import ndb

from blog.models import Comment
from blog.services.comment_service import service as comment_service
from main import markdown


class TagView:
	def __init__(self, entity):
		self.key = entity.key.urlsafe()
		self.tag = entity.tag
		self.category = CategoryView(entity.key.parent().get()).__dict__


class CategoryView:
	def __init__(self, entity):
		self.key = entity.key.urlsafe()
		self.category = entity.category
		self.slug = entity.slug


class CategorySummaryView:
	def __init__(self, entity):
		self.category = entity.category
		self.slug = entity.slug


class EntryView:
	@staticmethod
	def get_comments(entity):
		return comment_service.get_all_comments_by_ancestor(entity.key, sort=[-Comment.created], filters=[Comment.approved is True])

	def __init__(self, entity):
		self.title = entity.title
		self.summary = entity.summary
		self.post = markdown(entity.post)
		self.category = CategoryView(entity.key.parent().get()).__dict__
		self.tags = [TagView(tag.get()).__dict__ for tag in entity.tags]
		self.created = entity.created.isoformat()
		self.comment_count = 4
		# self.comments = [CommentView(comment).__dict__ for comment in self.get_comments(entity)]
		# self.comment_count = len(self.comments)


class EntrySummaryView:
	@staticmethod
	def get_comments_count(entity):
		return comment_service.count_comments_by_ancestor(entity.key)

	def __init__(self, entity):
		self.title = entity.title
		self.summary = entity.summary
		self.slug = entity.slug
		self.category = CategoryView(entity.key.parent().get()).__dict__
		self.tags = [TagView(tag.get()).__dict__ for tag in entity.tags]
		self.created = entity.created.isoformat()
		self.comment_count = 4
		# self.comment_count = self.get_comments_count(entity)


class EntryAdminView:
	@staticmethod
	def get_comments(entity):
		return comment_service.get_all_comments_by_ancestor(entity.key, sort=[-Comment.created],
		                                                    filter=[ndb.OR(ndb.AND(Comment.spam, Comment.approved),
		                                                                   Comment.approved)])

	def __init__(self, entity):
		self.key = entity.key.urlsafe()
		self.title = entity.title
		self.summary = entity.summary
		self.post = entity.post
		self.slug = entity.slug
		self.category = CategoryView(entity.key.parent().get()).__dict__
		self.tags = [TagView(tag.get()).__dict__ for tag in entity.tags]
		# self.comments = [CommentView(comment).__dict__ for comment in self.get_comments(entity)]


class MarkdownPreviewView:
	def __init__(self, preview):
		self.preview = markdown(preview)


class CommentView:
	def __init__(self, entity):
		self.key = entity.key.urlsafe()
		self.parentKey = entity.key.parent().urlsafe()
		self.comment = markdown(entity.comment)
		self.created = entity.created.isoformat()
		self.name = entity.name
		self.approved = entity.approved
		self.spam = entity.spam

		gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(entity.email.lower()).hexdigest() + "?"
		gravatar_url += urllib.urlencode({'d': 'mm', 's': str(80)})
		self.image = gravatar_url
