from server.server import auth, db, api
from werkzeug.security import check_password_hash
from flask import request, render_template, flash, session, redirect, url_for
from flask import g
from flask_restful import Resource
from server.app.forms import LoginForm
from server.app.forms import UserCreateForm, SessionCreateForm, PostCreateForm
from server.app.models import User, Post
from server.app.serializers import UserSerializer, PostSerializer


# Set the route and accepted methods
class SignInView(Resource):
	def get(self):
		# If sign in form is submitted
		form = LoginForm(request.form)

		# Verify the sign in form
		if form.validate():

			user = User.query.filter_by(email=form.email.data).first()

			if user and check_password_hash(user.password, form.password.data):
				session['user_id'] = user.id

				flash('Welcome %s' % user.name)

				return redirect(url_for('auth.home'))

			flash('Wrong email or password', 'error-message')

		return render_template("auth/signin.html", form=form)


@auth.verify_password
def verify_password(email, password):
	user = User.query.filter_by(email=email).first()
	if not user:
		return False
	g.user = user
	return user.password is password


class UserView(Resource):
	def post(self):
		form = UserCreateForm()
		if not form.validate_on_submit():
			return form.errors, 422

		user = User(form.email.data, form.password.data)
		db.session.add(user)
		db.session.commit()
		return UserSerializer(user).data


class SessionView(Resource):
	def post(self):
		form = SessionCreateForm()
		if not form.validate():
			return form.errors, 422

		user = User.query.filter_by(email=form.email.data).first()
		if user and user.password is form.password.data:
			return UserSerializer(user).data, 201
		return '', 401


class PostListView(Resource):
	def get(self):
		posts = Post.query.all()
		return PostSerializer(posts, many=True).data

	@auth.login_required
	def post(self):
		form = PostCreateForm()
		if not form.validate_on_submit():
			return form.errors, 422
		post = Post(form.title.data, form.body.data)
		db.session.add(post)
		db.session.commit()
		return PostSerializer(post).data, 201


class PostView(Resource):
	def get(id):
		posts = Post.query.filter_by(id=id).first()
		return PostSerializer(posts).data


api.add_resource(SignInView, '/api/auth/signin')

api.add_resource(UserView, '/api/users')
api.add_resource(SessionView, '/api/sessions')
api.add_resource(PostListView, '/api/posts')
api.add_resource(PostView, '/api/posts/<int:id>')
