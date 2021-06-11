#install the package
pip install docx2txt

#import the library
import docx2txt

#Read the docx file
MY_TEXT = docx2txt.process("/content/Document (3).docx")

print(MY_TEXT)