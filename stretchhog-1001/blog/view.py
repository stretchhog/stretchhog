__author__ = 'tvancann'


class TagView():
	def __init__(self, tag):
		self.key = tag.key.urlsafe()
		self.tag = tag.tag
		self.category = tag.category.get().category


class CategoryView():
	def __init__(self, category):
		self.key = category.key.urlsafe()
		self.category = category.category


class EntryView():
	def __init__(self, entry):
		self.key = entry.key.urlsafe()
		self.title = entry.title
		self.post = entry.post
		self.category = entry.category.get().category
		self.cat_key = entry.category.urlsafe()
		self.tags = [tag.get().tag for tag in entry.tags]
		# self.user = entry.user
		self.date_added = str(entry.date_added)
