import PyPDF4
import re

pdf = open("/home/catsquotl/Desktop/dnd5/Monster-Manual.pdf", 'rb')
read_pdf = PyPDF4.PdfFileReader(pdf)

info = read_pdf.getNumPages()
page = read_pdf.getPage(351)

rtxt = page.extractText()
santxt = rtxt.replace('\n', '')
ftxt = santxt.replace(',',':')

lis = re.findall(r'[\sA-z]* \w+: \d+', ftxt)

for l in lis:
    l = re.sub(r'[A-Z] ',' ',l)
    print(l)
