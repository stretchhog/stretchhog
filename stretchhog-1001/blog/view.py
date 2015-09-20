__author__ = 'tvancann'


class TagView:
	def __init__(self, entity):
		self.key = entity.key.urlsafe()
		self.tag = entity.tag
		self.category = entity.key.parent().get().category


class CategoryView:
	def __init__(self, category):
		self.key = category.key.urlsafe()
		self.category = category.category


class EntryView:
	@staticmethod
	def get_comments():
		return 0

	def __init__(self, entity):
		self.key = entity.key.urlsafe()
		self.title = entity.title
		self.summary = entity.summary
		self.post = entity.post
		self.category = CategoryView(entity.key.parent().get()).__dict__
		self.tags = [TagView(tag.get()).__dict__ for tag in entity.tags]
		self.date_added = entity.date_added.strftime('%Y, %d %B')
		self.comments = self.get_comments()


class EntrySummaryView:
	@staticmethod
	def get_number_of_comments():
		return 0

	def __init__(self, entity):
		self.key = entity.key.urlsafe()
		self.title = entity.title
		self.summary = entity.summary
		self.category = CategoryView(entity.category.get())
		self.tags = [TagView(entity.tag.get()) for tag in entity.tags]
		self.date_added = str(entity.date_added)
		self.nr_of_comments = self.get_number_of_comments()


class CommentView:
	def __init__(self, entity):
		self.comment = entity.comment
		self.user = entity.user.nickname()
		self.date_added = entity.date_added.strftime('%a, %d %b %Y %H:%M')
