def pullcontent(myfile):
	f = open(file,'r')
	newf = open(file,'a')
	for line in f:
		newf.write(line)
	return newf
