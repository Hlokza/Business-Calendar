


#split string into a list based on a charactor
eg = "hell,world"
def separate(s,q):
	t =[""]
	i = 0
	#get the lenth of the string
	l = len(s)
	print(l)
	for j in range(0,l):
		if s[j] == q:
			i += 1
			t.append("")
		else:	
			t[i] += s[j]
	return t	


#import data from csv format file
#fn is file name
#fm is file mode i.e r
#fs is the file separater i.e | or ,
def readCsv(fn,fm,fs):
	extFile = ""
	jq = ""
	s = []
	extFile =  open(fn,fm)
	jq = extFile.read()
	ss =separate(jq,"\n")
	for iq in ss:
		s.append(separate(iq,fs))
	extFile.close()
	return s	
	#print(s)
#In a different path
def readCsvPath(fn,fm,fs):
	extFile = ""
	jq = ""
	s = []
	with open(fn,fm) as extFile:  
		jq = extFile.read()
		ss =separate(jq,"\n")
		for iq in ss:
			s.append(separate(iq,fs))
	extFile.close()
	return s	
	#print(s)	

#This function checks if a string is a number
def isnumber(a):
	n = ["1","2","3","4","5","6","7","8","9","0"]
	al = "abcdefghijklnmopqrstuvwxyz"
	x = 0
	for i in a:
		if i in n:
			x += 0
		elif i in al:
			x += 1
			#print("Its false because: ",i)
	if x>0:
		return "false"
	elif x == 0:
		return "true"	