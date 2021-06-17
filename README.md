# Extracting text from PDF,docx and doc file:

import the required modules 
    
    import docx2txt
    import PyPDF2
    import io
    import codecs
    import os
    import glob
    import win32com.client
Creating the function for pdf, docx and doc.

Using the process module read the docx file and creat a file name to generate encode to text codecs open the new text file (utf-8) write my text and close function.


        MY_TEXT = docx2txt.process("RP/"+docxname)

Using the pdffilereader module read the pdf file and creat a file name to generate encode to text codecs open the new text file (utf-8) write my text and close function.         

        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)     


creating the function using the if statement, read and get the files and extract the text file from the pdf, docx and doc.

close the function.
