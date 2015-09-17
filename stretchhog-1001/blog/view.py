__author__ = 'tvancann'

from blog import service

class TagView():
	def __init__(self, tag):
		self.key = tag.key.urlsafe()
		self.tag = tag.tag
		self.category = tag.category.get().category

