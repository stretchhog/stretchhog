from flask import request, render_template
from flask.ext.restful import Resource
from main import api


class ComicCreate(Resource):
	def get(self):
		return render_template("comics/create.html")

	def post(self):
		print request.form['number']
		print request.form['title']
		print request.form['notes']


api.add_resource(ComicCreate, '/comic/create')
