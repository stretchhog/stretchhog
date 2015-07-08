from flask import g
from server.server import db

__author__ = 'Stretchhog'
# Import the database object (db) from the main application module
# We will define this inside /server/__init__.py in the next sections.

# Define a base model for other database tables to inherit
class Base(db.Model):
	__abstract__ = True

	id = db.Column(db.Integer, primary_key=True)
	date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
	date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())


# Define a User model
class User(Base):
	email = db.Column(db.String(128), nullable=False, unique=True)
	password = db.Column(db.String(192), nullable=False)
	posts = db.relationship('Post', backref='user', lazy='dynamic')

	# New instance instantiation procedure
	def __init__(self, email, password):
		self.email = email
		self.password = password

	def __repr__(self):
		return '<User %r>' % self.email


class Post(Base):
	title = db.Column(db.String(120), nullable=False)
	body = db.Column(db.Text, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __init__(self, title, body):
		self.title = title
		self.body = body
		self.user_id = g.user.id

	def __repr__(self):
		return '<Post %r>' % self.title
