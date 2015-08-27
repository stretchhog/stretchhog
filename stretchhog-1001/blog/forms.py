from flask.ext.wtf import Form
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

class ComicCreateForm(Form):
	number = IntegerField('number', validators=[DataRequired()])

class ComicDeleteForm(Form):
	number = IntegerField('number', validators=[DataRequired()])
