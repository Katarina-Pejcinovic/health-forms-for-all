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
annotation2 = AnnotationBuilder.rectangle(
    rect=(50, 550, 200, 650),
    interiour_color='#f52891'
)
writer.add_annotation(page_number=0, annotation=annotation)
writer.add_annotation(page_number=0, annotation=annotation2)

with open('output.pdf', 'wb') as outfile:
    writer.write(outfile)