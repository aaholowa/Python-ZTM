import PyPDF2
import sys

# stores every entry from command window besides the first in a list
inputs = sys.argv[1:]


def pdf_combine(pdf_list):
    merger = PyPDF2.PdfFileMerger()  # create merger object
    for pdf in pdf_list:
        merger.append(pdf)  # append pages to merger object
    merger.write("merged.pdf")  # save pdf with merged.pdf title


pdf_combine(inputs)
