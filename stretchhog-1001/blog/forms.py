from google.appengine.ext.ndb.key import Key

from wtforms.validators import DataRequired
from flask.ext.wtf import Form
from wtforms import StringField, SelectField, SelectMultipleField, HiddenField
from blog.models import Tag
from blog import service
from wtforms.widgets import TextArea


class EntryForm(Form):
	title = StringField(validators=[DataRequired()])
	summary = StringField(widget=TextArea(), validators=[DataRequired()])
	post = StringField(widget=TextArea(), validators=[DataRequired()])
	category = HiddenField()
	tags = SelectMultipleField()

	def __init__(self, key, *args, **kwargs):
		super(EntryForm, self).__init__(*args, **kwargs)
		self.category.data = key
		tags = service.get_all_tags(filter=[Tag.category == Key(urlsafe=key)])
		self.tags.choices = [(tag.key.urlsafe(), tag.tag) for tag in tags]


class CategoryForm(Form):
	category = StringField()


class TagForm(Form):
	tag = StringField()
	category = SelectField()

	def __init__(self, *args, **kwargs):
		super(TagForm, self).__init__(*args, **kwargs)
		categories = service.get_all_categories()
		self.category.choices = [(category.key.urlsafe(), category.category) for category in categories]
