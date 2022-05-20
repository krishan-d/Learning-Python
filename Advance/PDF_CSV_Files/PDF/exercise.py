import PyPDF2
import re

f = open('Find_the_Phone_Number.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(f)

print(pdf_reader.numPages)
rex = r'\d{3}.\d{3}.\d{4}'

all_text = ''
for n in range(pdf_reader.numPages):
    page = pdf_reader.getPage(n)
    page_text = page.extractText()

    all_text = all_text+' '+page_text


# print(re.findall(rex, all_text))
for match in re.finditer(rex, all_text):
    print(match)
