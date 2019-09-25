import PyPDF4
import re

pdf = open("/home/catsquotl/Desktop/dnd5/Monster-Manual.pdf", 'rb')
read_pdf = PyPDF4.PdfFileReader(pdf)
index = (351,352)
def get_index(pagenum):
    page = read_pdf.getPage(pagenum)
    rtxt = page.extractText()
    santxt = rtxt.replace('\n', '')
    ftxt = santxt.replace(',',':')
    tmp_lis = re.findall(r'[\sA-z]* \w+: \d+', ftxt)
    lis = []
    for l in tmp_lis:
        l = re.sub(r'[A-Z] ',' ',l)
        l = l.lstrip()
        lis.append(l)
    return lis

for n in index:
    print(get_index(n))

#if __name__ == '__main__':
