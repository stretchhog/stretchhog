from wtforms_alchemy import model_form_factory
from wtforms import PasswordField, StringField, Form  # BooleanField
from wtforms.validators import Email, DataRequired
from server.app.models import User, Post
from server.server import db

BaseModelForm = model_form_factory(Form)


class ModelForm(BaseModelForm):
	@classmethod
	def get_session(cls):
		return db.session


class UserCreateForm(ModelForm):
	class Meta:
		model = User


class SessionCreateForm(Form):
	email = StringField('email', validators=[DataRequired()])
	password = StringField('password', validators=[DataRequired()])


class PostCreateForm(ModelForm):
	class Meta:
		model = Post


class LoginForm(Form):
	email = StringField('Email Address', [Email(), DataRequired(message='Forgot your email address?')])
	password = PasswordField('Password', [DataRequired(message='Must provide a password. ;-)')])
