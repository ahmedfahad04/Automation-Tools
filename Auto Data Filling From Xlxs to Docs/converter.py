import os
import sys
import win32com.client as win32

import pandas as pd
from docxtpl import DocxTemplate

def convert_to_pdf(doc):
    word = win32.DispatchEx("Word.Application")
    new_name = os.path.splitext(doc)[0] + ".pdf"
    worddoc = word.Documents.Open(doc)
    worddoc.SaveAs(new_name, FileFormat=17)
    worddoc.Close()
    word.Quit()
    
# read the doc file 
data = pd.read_excel('data.xlsx')
doc = DocxTemplate("template.docx")

# operation for a single file
context = {'Name': 'Akash'}

# show the attributes
# remove all the extra spaces in the column names
data.columns = data.columns.str.strip()
names = []
i = 1

for name in data.Name:

    # make the context for the template
    context = {
        'name': name
    }

    doc.render(context)
    doc.save(f"Output/generated_doc{i}.docx")
    
    path_to_word_doc = os.path.join(os.getcwd(), f'Output/generated_doc{i}.docx')
    convert_to_pdf(path_to_word_doc)

    i += 1
    if i > 10:
        break
