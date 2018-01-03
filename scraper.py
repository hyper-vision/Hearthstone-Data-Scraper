from bs4 import BeautifulSoup as soup
from urllib import request
import urllib

# card_name = input("Enter the name of the card: ")

card_name = 'Kingsbane'
wikiUrl = 'https://hearthstone.gamepedia.com/{}'.format(card_name)
wikiUrl = urllib.parse.quote(wikiUrl, safe=":/")

pwnSearchUrl = "http://www.hearthpwn.com/search?search={}#t1:cards".format(card_name)
pwnSearchResult = request.urlopen(pwnSearchUrl)

try:


wiki_web_page = request.urlopen(wikiUrl)
wiki_content = wiki_web_page.read()
wiki_web_page.close()
wiki_page_soup = soup(wiki_content, "html.parser")

def getWiki():
	# mainContent = page_soup.find('div',{'id':'mw-content-text', 'class': 'mw-content-ltr'})
	# container = mainContent.find('span', {'class': 'mw-headline', 'id': 'Strategy'})

	return "Some random crap. Blah!"

def getImg():
	imgContent = wiki_page_soup.find('div', {'class': 'image'})
	return imgContent.a.img['src']
