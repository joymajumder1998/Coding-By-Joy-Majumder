import PyPDF2 
  
pdfFileObj = open('Introduction to Algorithms.pdf', 'rb') # creating a pdf file object   
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) # creating a pdf reader object 
numbers=pdfReader.numPages # printing number of pages in pdf file 
text=str()
for i in range(2,6):
	pageObj = pdfReader.getPage(i) # creating a page object 
	text = text+pageObj.extractText() # extracting text from page   
pdfFileObj.close() # closing the pdf file object 
print(text)
