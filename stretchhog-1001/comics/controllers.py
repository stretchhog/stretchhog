import io
from comics import crawler
from comics.forms import ComicCreateForm, ComicDeleteForm
from comics.models import Comic
from flask import request, render_template, make_response, redirect, send_file
from flask.ext.restful import Resource, abort
from main import api
from base64 import b64encode

comics = {}


class ComicDelete(Resource):
	def get(self, comic_number):
		Comic.query(Comic.number == comic_number).fetch(1)[0].delete()
		return redirect(api.url_for(ComicList), 301)


class ComicDetail(Resource):
	def get(self, comic_number):
		qry = Comic.query(Comic.number == comic_number)
		comic = qry.fetch(1)[0]
		return make_response(render_template('comics/detail.html', comic=comic))


class ComicList(Resource):
	def get(self):
		all = Comic.query().order(Comic.number).fetch()
		return make_response(
			render_template("comics/list.html", title="Comics", comics=all, form=ComicCreateForm()))

	def post(self):
		form = ComicCreateForm(data=request.get_json())
		if form.validate():
			pass
		else:
			abort(400)
		qry = Comic.query(Comic.number == form.number.data)
		if len(qry.fetch(1)) > 0:
			return make_response(render_template("409.html"))

		comic = Comic()
		comic.number = form.number.data
		comic.title = crawler.findTitle(comic.number)
		image = crawler.findImage(comic.number, comic.title)
		comic.image = b64encode(image) if image is not None else image
		comic.put()
		return redirect(api.url_for(ComicList), 301)


api.add_resource(ComicDelete, '/comics/delete<int:comic_number>', endpoint='comic_delete')
api.add_resource(ComicDetail, '/comics/<int:comic_number>', endpoint='comic_detail')
api.add_resource(ComicList, '/comics/list', endpoint='comic_list')
