__author__ = 'Stretchhog'

from marshmallow import Serializer, fields


class ComicSerializer(Serializer):
	class Meta:
		fields = ("id", "number", "title", "notes")
