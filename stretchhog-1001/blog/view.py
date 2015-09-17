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

