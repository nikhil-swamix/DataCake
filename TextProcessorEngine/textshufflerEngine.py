def sentence_tokens(string):
	#converts string to sentences in form of list
	sentences=[]
	# word_tokens=string.split()
	s=''
	for alpha in string:
		s=s + alpha 
		if alpha == '.':
			sentences.append(s)
			s=''
	return sentences


file = open('tempholdfile.txt', 'r').read()
word_vector= file.split()
bigstr= file.replace('\n',' ')

#temp is sentence wise array
temp=[]
temp=sentence_tokens(bigstr)

def swapper(list1):
	#leaves first 2 lines and 
	article=[];	article.append(list1[0]+list1[1])
	for i in range(3 , len(list1), 2):
		article.append( list1[i] )
		article.append( list1[i-1] )
	bigpiece=''

	#below loop joins article elements to big sting
	for sent in article:
		bigpiece=bigpiece+sent
	print(bigpiece)
	return bigpiece

final=swapper(temp)
open('rewritten.txt', 'w').write(final)
# print(swapper(temp))
