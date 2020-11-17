# import spacy
# nlp = spacy.load("en_core_web_sm")
# doc = nlp("Apple is looking at buying U.K. startup for $1 billion")
# for ent in doc.ents:
#     print(ent.text, ent.start_char, ent.end_char, ent.label_)


#+++++++++++++++++++++++++++++++++++++++++++++++>>> REGEX
# import re
# text='hewlett-packard-$3000,"enterprise partners with wipro to deliver hybrid cloud with hpe greenlake'
# matched=re.sub(r'[\W]',' ',text).split()
# print("-".join(matched))


#+++++++++++++++++++++++++++++++++++++++++++++++>>> BS4 UNIT TESTS

from bs4 import BeautifulSoup as soup
import time,os

data2=open('dummy.html','r',encoding='utf-8').read()

# data2='<p><img alt="image20" class="aligncenter size-full wp-image-16018 lazyloaded" data-ll-status="loaded" height="770" sizes="(max-width: 1024px) 100vw, 1024px" src="https://neilpatel.com/wp-content/uploads/2016/05/image20-6.png" srcset="https://neilpatel.com/wp-content/uploads/2016/05/image20-6.png 1024w, https://neilpatel.com/wp-content/uploads/2016/05/image20-6-350x263.png 350w, https://neilpatel.com/wp-content/uploads/2016/05/image20-6-768x578.png 768w, https://neilpatel.com/wp-content/uploads/2016/05/image20-6-700x526.png 700w" width="1024"/></p>'
mysoup=soup(data2,'lxml')


def tag_unwrapper(tagname,input):
	s=s.unwrap()
	pass


def extract_body(mysoup,remove_img=1):
	parafind=mysoup.findAll('p')
	lastParentLen=0
	theRealParent=[]
	try:
		while mysoup.find('p'):
			parent=mysoup.find('p').parent.extract()
			if lastParentLen<len(parent):
				theRealParent=parent
				lastParentLen=len(parent)
		if remove_img:
			[x.decompose() for x in theRealParent.findAll('img')]
		return str(theRealParent)
	except Exception as e:
		...
	# return str(mysoup.p.parent.extract())

tarbody=extract_body(mysoup)
print(tarbody)

# links= mysoup.findAll('a')
# print(links)
































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































