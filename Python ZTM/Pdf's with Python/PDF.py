import PyPDF2

# get pf in dir and read binary
with open('dummy.pdf', 'rb') as file:
    # make an object reader and use the PdfFileReader method
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)
    print(reader.getPage(0))

    # page object
    page = reader.getPage(0)  # save page 1
    # rotate page 1 (this is just stored in mmemeory at this instant)
    page.rotateCounterClockwise(90)

    writer = PyPDF2.PdfFileWriter()  # create a writer object
    writer.addPage(page)  # add titlted page to writer object

    with open('tiltled.pdf', 'wb') as new_file:
        writer.write(new_file)
