import glob
import win32com.client
import os

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