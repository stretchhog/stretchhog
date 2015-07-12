from string import lower
from google.appengine.api import urlfetch
from bs4 import BeautifulSoup


def findTitle(number):
	url = 'http://suskeenwiske.ophetwww.net/albums/4kl/lijst.php'
	source_code = urlfetch.fetch(url)
	soup = BeautifulSoup(source_code.content, "html.parser")
	for ol in soup.findAll('ol'):
		for li in ol.findAll('a', href=True):
			if str(number) in li['href']:
				return unicode(li.contents[0])


def findImage(number):
	img_url = 'http://www.suskeenwiske.be/wp-content/uploads/2013/02/' + str(number) + '.jpg'
	return urlfetch.Fetch(img_url).content
