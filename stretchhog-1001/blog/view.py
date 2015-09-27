import markdown2

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
		self.date_added = entity.date_added.strftime('%Y, %d %B')
		self.comments = [CommentView(comment).__dict__ for comment in self.get_comments(entity)]
		self.comment_count = len(self.comments)


class EntryPostView:
	def __init__(self, entity):
		self.post = markdown(entity.post)


class CommentView:
	def __init__(self, entity):
		self.comment = entity.comment
		self.user = entity.user.nickname()
		self.date_added = entity.date_added.strftime('%a, %d %b %Y %H:%M')
