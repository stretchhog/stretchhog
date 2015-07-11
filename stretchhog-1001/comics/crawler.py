import httplib
from google.appengine.api import urlfetch
from bs4 import BeautifulSoup
import requests

imagePath = "covers/suske_en_wiske/"


def findTitle(number):
	url = 'http://suskeenwiske.ophetwww.net/albums/4kl/lijst.php'
	source_code = requests.get(url)
	soup = BeautifulSoup(source_code.text, "html.parser")
	for ol in soup.findAll('ol'):
		for li in ol.findAll('a', href=True):
			if str(number) in li['href']:
				return unicode(li.contents[0])


def findImage(number):
	image = str(number) + ".gif"
	host = "suskeenwiske.ophetwww.net"
	path = "/albums/pics/4kl/groot/" + image
	alternatePath = "/albums/pics/4kl/" + image

	if getStatusCode(host, path) == 200:
		url = "http://" + host + path
	elif getStatusCode(host, alternatePath) == 200:
		url = "http://" + host + alternatePath
	else:
		return None
	return urlfetch.Fetch(url).content
	# response = urllib2.urlopen(url)
	# img = response.read()
	# response.close()
	# return img


def readNumbers(filename):
	with open(filename) as f:
		lines = f.readlines()
	return [line.rstrip() for line in lines]


def getStatusCode(host, path="/"):
	try:
		conn = httplib.HTTPConnection(host)
		conn.request("GET", path)
		return conn.getresponse().status
	except StandardError:
		return None
