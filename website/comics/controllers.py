from flask.ext.restful import Resource

from website.comics.forms import ComicAddForm
from website.comics.models import Comic
from website.comics.serializers import ComicSerializer
from website.server import auth, db, api


class ComicListView(Resource):
	def get(self):
		comics = Comic.query.all()
		return ComicSerializer(comics, many=True).data

# api.add_resource(ComicListView, '/comics')
