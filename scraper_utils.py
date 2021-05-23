from datetime import datetime
import random,time,re
from mxproxy import mx
from bs4 import Comment
# mx.auto_pip('spacy')

def remove_comments(soup,mode='soup/regex'):
	if type(soup).__name__ != 'BeautifulSoup': #try converting to native soup/tag
		try:
			soup = mx.make_soup(soup)
		except :
			pass

	for node in soup.find_all(text=lambda s: isinstance(s, Comment)):
		node.extract()

	if mode == 'regex':
		return re.sub(r'<!.*?->','', string)
	return soup


def remove_attributes(soup,keep=['href'],lengthkill={'href':150}):
	if type(soup).__name__ == 'str':
		soup = mx.make_soup(soup)
	for tag in soup.findAll():
		attrs=list(tag.attrs)
		for y in attrs:
			if y not in keep:
				del tag.attrs[y]
			if y in lengthkill and len(tag.attrs[y]) > lengthkill[y]:
				del tag.attrs[y]
	return soup


def remove_empty_tags(soup):
	[x.extract() for x in soup.findAll() if x.text=='']
	return soup


def make_timestamp(expireAfterDays=(500,50000)):
	futuretime=time.time()+(random.randrange(*expireAfterDays)*60*60*24)
	tobj=datetime.fromtimestamp(futuretime)
	timestrattr=tobj.strftime('%Y-%m-%dT%H:%M:%S') 
	timestrtext=tobj.strftime('%Y-%m-%d %H:%M:%S %A')
	timetag=f'<time datetime="{timestrattr}">Expires on {timestrtext}</time>'
	return timetag


def sanitize_text(text): 
	return re.sub(	r'\n|\t','',text)


def file_namer(text): 
	return "-".join(re.sub(r'[\W]',' ',text).split()).lower()


def extract_body(mysoup,soupify=True,removeComments=True,removeAttributes=True,removeEmpty=True):
	# NOTE: extract body is a heavy function and is destructive
	# recommended to call this at last while extracting info from page
	[x.decompose() for x in mysoup.findAll('a',href=(False,lambda x: '#' in x) )]
	lastParentLen=0
	theRealParent=[]
	try:
		while mysoup.find('p'):
			parent=mysoup.find('p').parent.extract()
			if lastParentLen<len(parent):
				theRealParent=parent
				lastParentLen=len(parent)

		# print(theRealParent)
		if removeComments:
			theRealParent=remove_comments(theRealParent)

		if removeAttributes:
			theRealParent=remove_attributes(theRealParent)

		if removeEmpty:
			theRealParent=remove_empty_tags(theRealParent)

		if not soupify:
			return str(theRealParent)

		return theRealParent

	except Exception as e:
		raise e
		return f'error parsing body::{e}'


def get_author_info(mysoup):# use random name generator from https://github.com/philipperemy/name-dataset
	def r(k=24):
		return "".join(random.choices(list('1234567890abcdef'),k=24))
	authorgrav=f'https://www.gravatar.com/avatar/{r()}?s=32&d=identicon&r=PG'
	authsoup=mysoup.find(class_=lambda x: x and 'author' in x)
	if not authsoup: 
		return {'name':r(), 'image':authorgrav, 'links':''}

	authorlinks=list({x['href'] for x in authsoup.findAll('a',href=True)})
	try:
		authorname=authsoup.findAll('a',text=True)[0].text
	except:
		authorname= r()
	authdict={
		'name':authorname,
		'image':authorgrav,
		'links':authorlinks}
	return authdict

def multi_replace(text,dictonary={'<':' <','>':'> ',}):
	for repl in dictonary:
		text=text.replace(repl,dictonary[repl])
	return text

def explain_word(text,charsabove=6):
	...

if __name__ == '__main__' :
	soup=mx.get_page_soup('https://www.helpguide.org/articles/pets/health-benefits-of-walks-with-your-dog.htm')
	soup=mx.get_page_soup('https://edition.cnn.com/2021/05/23/europe/italy-cable-car-accident-intl/index.html')


	[x.decompose() for x in soup.findAll(['script','head','style','svg','noscript'])]#remove unwanted
	body=extract_body(soup)
	print(body)


	# url='https://en.wikipedia.org/wiki/Google_AdSense'
	# mysoup=soup(requests.get(url).text,features='lxml')
	# result=extract_body(mysoup,return_text=False).findAll('p')
	# print(result)

	# print(multi_replace(result))

	# retest=re.match(r'[\w]*','administered,').group()
	# print(retest)
	...