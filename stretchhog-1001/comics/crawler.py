from string import lower
from google.appengine.api import urlfetch
from bs4 import BeautifulSoup


def findTitle(number):
	url = 'http://suskeenwiske.ophetwww.net/albums/4kl/lijst.php'
	source_code = urlfetch.fetch(url)
	print source_code.content
	soup = BeautifulSoup(source_code.content, "html.parser")
	for ol in soup.findAll('ol'):
		for li in ol.findAll('a', href=True):
			if str(number) in li['href']:
				return unicode(li.contents[0])


def findImage(number, title):
	# host = 'http://www.suskeenwiske.be/comics/'
	# parsed_title = lower(title).replace(" ", "-")
	# path = str(number) + '-' + parsed_title
	# url = host + path

	# response = urlfetch.fetch(url)
	#
	# soup = BeautifulSoup(response.content, 'html.parser')
	# div = soup.findAll('div', {'class': 'singl-img'})[0]
	# img = div.findAll("img")[0]
	# img_url = img['src']

	img_url = 'http://www.suskeenwiske.be/wp-content/uploads/2013/02/' + str(number) + '.jpg'
	return urlfetch.Fetch(img_url).content
