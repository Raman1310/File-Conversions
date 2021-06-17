import docx2txt
import PyPDF2
import io
import codecs
import os
import glob
import win32com.client

def docx(docxname,txtname):
    MY_TEXT = docx2txt.process("RP/"+docxname)
    txtfile=txtname+str(".txt")
    f= codecs.open(txtfile,"w+","utf-8")
    f.write(MY_TEXT)
    f.close()
def pdf(pdfname,txtname):
    pdfFileObj = open('RP/'+pdfname, 'rb') 
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)     
    pageObj = pdfReader.getPage(0) 
    txt=pageObj.extractText()
    txtfile=txtname+str(".txt")
    f= codecs.open(txtfile,"w+","utf-8")
    f.write(txt)
    f.close()
    pdfFileObj.close()
def doc():
    word = win32com.client.Dispatch("Word.Application")
    word.visible = 0
    for i, doc in enumerate(glob.iglob("*.doc")):
        in_file = os.path.abspath(doc)
        wb = word.Documents.Open(in_file)
        print(in_file)
        out_file = str(in_file)[:-4] + ".docx"
        print(out_file)
        wb.SaveAs2(out_file, FileFormat=16) # file format for docx
        wb.Close()
    word.Quit()
def RP():
    entries = os.listdir('RP/')
    for entry in entries:
        # print(entry)
        files=os.path.splitext(entry)
        print(files[0],files[1])
        if str(files[1])==".pdf":
            pdf(entry,str(files[0]))
            print("pdf")
        if str(files[1])==".docx":
            docx(entry,str(files[0]))
            print("docx")
RP()
doc()