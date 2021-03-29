from bs4 import  BeautifulSoup as soup
import requests
import html5lib
headers = {'User-Agent': 'Mozilla'}

def write_this(title,content):
	f=open(title+".txt","w+")
	f.write(content)

def bs_all_content_of(tag):
	pageObject	= soup(rawpage,features="html5lib")
	fullcontent=''
	content=pageObject.findAll('p')
	for i in content:
		fullcontent += i.text
	return fullcontent

def remove_duplicates(x):
	  return list(dict.fromkeys(x))

url="https://www.investopedia.com/terms/c/credit.asp"
rawpage		= requests.get(url,headers=headers).text
pageObject	= soup(rawpage,features="html5lib")

commonWords='the at there some my of be use her than and this an would first a have each make water to from which like been in or she him call is one do into who you had how time oil that by their has its it word if look now he but will two find was not up more long for what other write down on all about go day are were out see did as we many number get with when then no come his your them way made they can these could may I said so people part'
commonWords= set(commonWords.split())

class pageStats:
	def __init__(self , pageText):  
		self.pageText  = pageText
		self.wordArray = pageText.split()
		self.wordCount = len(pageText.split())

	def keywords(self):
		duplicateWordArray=self.wordArray
		for i in range(len(duplicateWordArray)):
			if duplicateWordArray[i] in commonWords:
				duplicateWordArray[i]=''

		return remove_duplicates(duplicateWordArray) 
		

pContent =bs_all_content_of('p')
pageMetrics = pageStats(pContent)

print(pageMetrics.keywords())