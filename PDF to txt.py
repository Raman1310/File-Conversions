#install the PDF package
pip install PyPDF2

#import the library
import PyPDF2 
    
#Read the PDF file
pdfFileObj = open('/content/drive/MyDrive/RAM LOGO.pdf', 'rb') 
    
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
    
    
pageObj = pdfReader.getPage(0) 
    
print(pageObj.extractText()) 
    
pdfFileObj.close()