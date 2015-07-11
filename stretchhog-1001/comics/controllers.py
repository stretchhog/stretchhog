from google.appengine.api import images
from comics import crawler
from comics.forms import ComicCreateForm
from comics.models import Comic
from flask import request, render_template, make_response, url_for, redirect, send_file
from flask.ext.restful import Resource, abort
from main import api

comics = {}


class ComicDetail(Resource):
	def get(self, comic_number):
		comic = Comic.query(Comic.number == comic_number).order()
		return send_file(comic.fetch(1)[0].image, mimetype='image/gif')

	def put(self, comic_id):
		pass

	def delete(self, comic_id):
		pass


class ComicList(Resource):
	def get(self):
		all = Comic.query().order(Comic.number)
		return make_response(render_template("comics/list.html", title="Comics", comics=all))


class ComicCreate(Resource):
	def get(self):
		return make_response(render_template("comics/create.html", title='Add a comic', form=ComicCreateForm()))

	def post(self):
		form = ComicCreateForm(data=request.get_json())
		if form.validate():
			pass
		else:
			abort(400)
		comic = Comic()
		comic.number = form.number.data
		comic.title = crawler.findTitle(comic.number)
		image = crawler.findImage(comic.number)
		comic.image = image
		#comic.thumb = images.resize(image, 32, 32)
		comic.put()

		return redirect(url_for('/comics/list'))


api.add_resource(ComicDetail, '/comics/<int:comic_number>')
api.add_resource(ComicCreate, '/comics/create')
api.add_resource(ComicList, '/comics/list')
