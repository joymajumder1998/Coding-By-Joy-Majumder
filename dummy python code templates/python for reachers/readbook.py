def readbook(path):
	"""Read a book and return it as a string"""
	with open(path,"r",encoding="utf-8") as fp:
		text=fp.read()
		text=text.replace("\n","")#.replace("\r","")
	fp.close
	return text

x="Introduction to Algorithms.pdf"
text=readbook(x)
print(text)
