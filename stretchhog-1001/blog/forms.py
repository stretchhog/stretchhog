from wtforms.validators import DataRequired
from flask.ext.wtf import Form
from wtforms import StringField, SelectField, SelectMultipleField, HiddenField

from blog import service


class BlogEntryCreateForm(Form):
	title = StringField(validators=[DataRequired()])
	post = StringField(validators=[DataRequired()])
	category = HiddenField()
	tags = SelectMultipleField()
	user = StringField(validators=[DataRequired()])


class CategoryCreateForm(Form):
	category = StringField()


class TagCreateForm(Form):
	tag = StringField()
	categories = service.get_all_categories()
	category = SelectField(choices=[(category.key.urlsafe(), category.category) for category in categories])