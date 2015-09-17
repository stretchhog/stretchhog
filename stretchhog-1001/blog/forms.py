from wtforms.validators import DataRequired
from flask.ext.wtf import Form
from wtforms import StringField, SelectField, SelectMultipleField, HiddenField

from blog import service


class BlogEntryCreateForm(Form):
	def __init__(self, *args, **kwargs):
		super(BlogEntryCreateForm, self).__init__(*args, **kwargs)

	title = StringField(validators=[DataRequired()])
	post = StringField(validators=[DataRequired()])
	category = HiddenField()
	tags = SelectMultipleField()
	user = StringField(validators=[DataRequired()])


class CategoryForm(Form):
	category = StringField()


class TagForm(Form):
	tag = StringField()
	category = SelectField()

	def __init__(self, *args, **kwargs):
		super(TagForm, self).__init__(*args, **kwargs)
		categories = service.get_all_categories()
		self.category.choices = [(category.key.urlsafe(), category.category) for category in categories]
