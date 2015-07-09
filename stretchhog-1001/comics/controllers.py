from flask.ext.restful import Resource

class ComicListView(Resource):
	def get(self):
		comics = Comic.query.all()
		return ComicSerializer(comics, many=True).data

api.add_resource(ComicListView, '/comics')
