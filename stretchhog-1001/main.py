import os
from google.appengine.api import users
from flask import Flask, session, render_template, make_response, redirect
from flask.ext.restful import Api, Resource
from flask.ext.triangle import Triangle
import wtforms_json
from flask_jsglue import JSGlue
import mistune
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

wtforms_json.init()

base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
JSGlue(app)
Triangle(app)
app.config['DEBUG'] = True
app.config['WTF_CSRF_ENABLED'] = False
app.config['SECRET_KEY'] = 'you-will-never-guess'

api = Api(app)


class HighlightRenderer(mistune.Renderer):
	def block_code(self, code, lang):
		if not lang:
			return '\n<pre><code>%s</code></pre>\n' % mistune.escape(code)
		lexer = get_lexer_by_name(lang, stripall=True)
		formatter = HtmlFormatter()
		return highlight(code, lexer, formatter)


renderer = HighlightRenderer()
markdown = mistune.Markdown(renderer=renderer)


@app.before_request
def before_request():
	user = users.get_current_user()
	if user:
		session['logged_in'] = True
		session['user_email'] = user.email()
		session['is_admin'] = users.is_current_user_admin()
	else:
		session['logged_in'] = False


class Intro(Resource):
	def get(self):
		return make_response(render_template("intro.html"))


class Main(Resource):
	def get(self):
		return make_response(render_template("index.html"))


class Login(Resource):
	def get(self):
		return redirect(users.create_login_url(dest_url='/'))


class Logout(Resource):
	def get(self):
		return redirect(users.create_logout_url(dest_url='/'))


api.add_resource(Main, '/', endpoint='home')
api.add_resource(Intro, '/intro', endpoint='intro')
api.add_resource(Login, '/login', endpoint='login')
api.add_resource(Logout, '/logout', endpoint='logout')

from blog import handler


@app.after_request
def after_request(response):
	response.headers.add('Access-Control-Allow-Origin', '*')
	response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
	response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
	return response
