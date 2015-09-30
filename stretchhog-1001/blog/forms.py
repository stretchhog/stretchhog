from wtforms.validators import DataRequired, ValidationError, Email
from flask.ext.wtf import Form
from wtforms import StringField, SelectField, SelectMultipleField, TextAreaField, BooleanField
from blog.services.tag_service import service as tag_service
from blog.services.category_service import service as category_service
from HTMLParser import HTMLParser


class EntryForm(Form):
	title = StringField()
	summary = TextAreaField()
	post = TextAreaField()
	category = SelectField()
	tags = SelectMultipleField()

	def __init__(self, *args, **kwargs):
		super(EntryForm, self).__init__(*args, **kwargs)
		categories = category_service.get_all_categories()
		self.category.choices = [(cat.key.urlsafe(), cat.category) for cat in categories]
		tags = tag_service.get_all_tags()
		self.tags.choices = [(tag.key.urlsafe(), tag.tag) for tag in tags]

	@staticmethod
	def from_json(json):
		form = EntryForm()
		form.title.data = json['title']
		form.summary.data = json['summary']
		form.post.data = json['post']
		form.category.data = json['category']
		form.tags.data = json['tags']
		return form


class CategoryForm(Form):
	category = StringField(validators=[DataRequired()])

	@staticmethod
	def from_json(json):
		form = CategoryForm()
		form.category.data = json['category']
		return form


class TagForm(Form):
	tag = StringField()
	category = SelectField()

	def __init__(self, *args, **kwargs):
		super(TagForm, self).__init__(*args, **kwargs)
		categories = category_service.get_all_categories()
		self.category.choices = [(cat.key.urlsafe(), cat.category) for cat in categories]

	@staticmethod
	def from_json(json):
		form = TagForm()
		form.tag.data = json['tag']
		form.category.data = json['category']
		return form


class HTMLValidator(HTMLParser):
	def __init__(self, message=None):
		HTMLParser.__init__(self)
		if not message:
			message = u'HTML tags are not allowed'
		self.message = message

	def handle_starttag(self, tag, attrs):
		raise ValidationError(self.message)

	def __call__(self, form, field):
		self.feed(field.data)


class CommentForm(Form):
	parent = StringField(validators=[DataRequired()])
	name = StringField(validators=[DataRequired()])
	email = StringField(validators=[DataRequired(), Email()])
	comment = TextAreaField(validators=[DataRequired('Please enter your comment.'), HTMLValidator()])
	approved = BooleanField()
	spam = BooleanField()

	@staticmethod
	def from_json(json):
		form = CommentForm()
		form.parent.data = json['parentKey']
		form.name.data = json['name']
		form.email.data = json['email']
		form.comment.data = json['comment']
		return form
