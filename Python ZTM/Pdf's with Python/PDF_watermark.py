import PyPDF2

# open pdf file you want to stamp
template = PyPDF2.PdfFileReader(open('merged.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))  # open stamp
combined = PyPDF2.PdfFileWriter()  # create combined object

# lopp through the range of pages in the pdf document
for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    combined.addPage(page)  # add water marked page to combined pdf

with open('watermarked_pdf.pdf', 'wb') as file:
    combined.write(file)
