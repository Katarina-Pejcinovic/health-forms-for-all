from pypdf import PdfReader, PdfWriter
from pypdf.generic import AnnotationBuilder

reader = PdfReader('intake1.pdf')
n_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()
print(text)

writer = PdfWriter()
writer.add_page(page)

annotation = AnnotationBuilder.text(
    (100, 200, 300, 400),
    "Hello world\nthis is the second line"
)
writer.add_annotation(page_number=0, annotation=annotation)

with open('output.pdf', 'wb') as outfile:
    writer.write(outfile)