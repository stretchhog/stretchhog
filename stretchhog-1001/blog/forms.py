from google.appengine.ext.ndb.key import Key
from blog.views import EntryView
from wtforms.validators import DataRequired
from flask.ext.wtf import Form
from wtforms import StringField, SelectField, SelectMultipleField, HiddenField, TextField, TextAreaField, BooleanField
from blog.models import Tag
from blog import service
from wtforms.widgets import TextArea


class EntryForm(Form):
	title = StringField(validators=[DataRequired()])
	summary = TextAreaField(validators=[DataRequired()])
	post = TextAreaField(validators=[DataRequired()])
	category = SelectField(validators=[DataRequired()])
	tags = SelectMultipleField()

	def __init__(self, *args, **kwargs):
		super(EntryForm, self).__init__(*args, **kwargs)
		categories = service.get_all_categories()
		self.category.choices = [(cat.key.urlsafe(), cat.category) for cat in categories]
		tags = service.get_all_tags()
		self.tags.choices = [(tag.key.urlsafe(), tag.tag) for tag in tags]

	@staticmethod
	def from_json(json, put_mode):
		form = EntryForm()
		form.title.data = json['title']
		form.summary.data = json['summary']
		form.post.data = json['post']
		if put_mode:
			form.category.data = json['category']['key']
			form.tags.data = [tag['key'] for tag in json['tags']]
		else:
			form.category.data = json['category']
			form.tags.data = json['tags']
		return form


class CategoryForm(Form):
	category = StringField(validators=[DataRequired()])

	@staticmethod
	def from_json(json, put_mode):
		form = CategoryForm()
		form.category.data = json['category']
		return form


class TagForm(Form):
	tag = StringField()
	category = SelectField(validators=[DataRequired()])

	def __init__(self, *args, **kwargs):
		super(TagForm, self).__init__(*args, **kwargs)
		categories = service.get_all_categories()
		self.category.choices = [(cat.key.urlsafe(), cat.category) for cat in categories]

	@staticmethod
	def from_json(json, put_mode):
		form = TagForm()
		if put_mode:
			form.category.data = json['category']['key']
		else:
			form.tag.data = json['tag']
			form.category.data = json['category']
		return form


class CommentForm(Form):
	comment = TextAreaField(validators=[DataRequired('Please enter your comment.')])
	parent = StringField(validators=[DataRequired()])
	email = StringField(validators=[DataRequired()])
	name = StringField(validators=[DataRequired()])
	approved = BooleanField()
	spam = BooleanField()

	@staticmethod
	def from_json(json, put_mode):
		form = CommentForm()
		form.parent.data = json['parentKey']
		form.email.data = json['email']
		form.name.data = json['name']
		form.comment.data = json['comment']
		if put_mode:
			form.approved.data = json['approved']
			form.spam.data = json['spam']
		return form
