import os

from google.appengine.api import users

from flask import Flask, session, render_template, make_response, redirect
from flask.ext.restful import Api, Resource
from flask.ext.markdown import markdown
import wtforms_json
from flask_jsglue import JSGlue


wtforms_json.init()

base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
markdown(app)
JSGlue(app)
app.config['DEBUG'] = True
app.config['WTF_CSRF_ENABLED'] = False
app.config['SECRET_KEY'] = 'you-will-never-guess'

api = Api(app)


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
