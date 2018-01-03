from bs4 import BeautifulSoup as soup
from urllib import request
import urllib

def getPage(card_name): 
	card_name = card_name.title()
	print(card_name)
	wikiUrl = 'https://hearthstone.gamepedia.com/{}'.format(card_name.strip())
	wikiUrl = urllib.parse.quote(wikiUrl, safe=":/")

	print(wikiUrl)

	pwnSearchUrl = "http://www.hearthpwn.com/search?search={}#t1:cards".format(card_name)
	pwnSearchResult = request.urlopen(pwnSearchUrl)


	wiki_web_page = request.urlopen(wikiUrl)
	wiki_content = wiki_web_page.read()
	wiki_web_page.close()
	wiki_page_soup = soup(wiki_content, "html.parser")
	return wiki_page_soup

def getWiki():
	# mainContent = page_soup.find('div',{'id':'mw-content-text', 'class': 'mw-content-ltr'})
	# container = mainContent.find('span', {'class': 'mw-headline', 'id': 'Strategy'})
	return "Some random crap. Blah!"

def getImg(card_name):
	wiki_page_soup = getPage(card_name)
	imgContent = wiki_page_soup.find('div', {'class': 'image'})
	return imgContent.a.img['src']

