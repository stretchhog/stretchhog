from wtforms_alchemy import model_form_factory, ModelForm
from wtforms import PasswordField, StringField, Form  # BooleanField


BaseModelForm = model_form_factory(Form)


class ComicAddForm(ModelForm):
	class Meta:
		model = Comic
