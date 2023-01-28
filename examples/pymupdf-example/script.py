import fitz, os

def rgb_to_stroke(rgb):
    return tuple([x / 255 for x in rgb])

script_path = os.path.dirname(os.path.realpath(__file__))
document = fitz.open(script_path + '/../inputs/intake1.pdf')

for page in document:

    search_text = 'please stop filling out the form'
    instances = page.search_for(search_text)

    for inst in instances:

        page.add_text_annot(inst.top_right, 'McDonald\'s\nBurger King')

        highlight = page.add_highlight_annot(inst)
        highlight.set_colors({'stroke': rgb_to_stroke((255, 108, 79)), 'fill': None})
        highlight.update()

document.save(script_path + '/output.pdf')