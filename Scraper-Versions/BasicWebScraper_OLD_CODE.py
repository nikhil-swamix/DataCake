import html5lib,requests
import threading
from bs4 import BeautifulSoup as soup
import random

def read_this (path):
	a=''
	f=open(path,'r',errors='ignore')
	a+=f.read()
	return a
def write_this (path,data):
	f=open(path,'a+',errors='ignore')
	f.write(data)

def get_links(markup):
	unqlinks=[]
	soups=soup(markup,features="html5lib")
	post_links=soups.findAll("a",href=True)
	for i in post_links:
		url=i['href']
		unqlinks.append(url)
	unqlinks = list(set(unqlinks))
	return unqlinks

def get_p(Pagetext):
	soups=soup(Pagetext,features="html5lib")
	P=soups.findAll("p")
	pagecontent=[i.text for i in P]
	return " ".join(pagecontent)

def open_page(url):
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	update_visited(url)
	fullText=requests.get(url,headers=headers).text
	print(threading.current_thread().getName(), " Just Visited : ", url)
	return fullText

def update_visited(link):
	visited.add(link)
	write_this('visited.txt',"\n"+link)

def update_found(link_list):
	for link in link_list:
		found.add(link)
		write_this('found.txt',"\n"+link)

def allowedToVisit(i,inp):
	flag=0
	for x in inp:
		if i == x :	flag=1
		else: pass
	return flag

def filterAllowedList(list_input):
	filtered=[]
	for i in onlyVisit:
		for j in list_input:
			try:
				if i in j.split('/')[2]:
					filtered.append(j)
			except : pass
	return filtered

#SETUP
FILENAME='CrawledData.txt'
SpeedMultiplier=25
onlyVisit=['https://www.livemint.com/']

#DECLARATION
#these are the memory files of this engine #to keep track of which website was visited
found=set( read_this('found.txt').split('\n') )
visited=set( read_this('visited.txt').split('\n') )
linkBuffer=list(found-visited)

#STATUS CHECK
print("visited={}\n  | Pending URLS {}".format(len(visited),len(found)) )

def explorer():
	#softly scans the webpage and builds an index of which url to visit
	global linkBuffer,onlyVisit
	global found,visited
	linkBuffer=list(found-visited)	
	for i in linkBuffer:
		try: 	currentPage=open_page(random.choice(linkBuffer))
		except 	Exception as s: print(s)

		write_this(FILENAME, get_p(currentPage)+'\n\n' )
		lHolder=filterAllowedList( get_links(currentPage) ) 
		update_found(lHolder)
		linkBuffer=list(found-visited)	


def visitor(index):
	global linkBuffer
	global found,visited
	linkBuffer=list(found-visited)	
	for i in linkBuffer:
		try:
			currentPage=open_page(random.choice(linkBuffer))
			write_this(FILENAME, get_p(currentPage)+'\n\n' )
		except :
			print('page skipped')
			pass
		linkBuffer=list(found-visited)	

#START
threadBoard=[]
for i in range(SpeedMultiplier):
	threadBoard.append(threading.Thread(target=visitor,args=(i,) ))
	threadBoard[i].start()
	print('Thread-',i,' HasBeenStarted')




