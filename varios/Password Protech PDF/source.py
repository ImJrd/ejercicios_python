from PyPDF2 import PdfFileWriter, PdfFileReader
import getpass

pdfwriter=PdfFileWriter()
pdf=PdfFileReader("one.pdf")
for page_num in range(pdf.numPages):
  pdfwriter.addPage(pdf.getPage(page_num))
passw=getpass.getpass(prompt='Enter Password: ')
pdfwriter.encrypt(passw)
with open('new.pdf','wb') as f:
  pdfwriter.write(f)
  f.close()

#pip install pypdf2