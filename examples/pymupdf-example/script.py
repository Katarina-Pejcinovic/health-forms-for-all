import fitz, os

def rgb_to_stroke(rgb):
    return tuple([x / 255 for x in rgb])

script_path = os.path.dirname(os.path.realpath(__file__))
document = fitz.open(script_path + '/../inputs/intake1.pdf')
bad_words ={'Parent': "parent(s)/guardian", 'Mother/Father': "parent(s)/Guardian", 
'sex': "gender assigned at birth", 'spouse': 'partner(s)', 'son/daughter': 'child', 
'name': 'legal name and chosen name', 'marital status': 'relationship status'}

for page in document:
    for key in bad_words.keys():
        instances = page.search_for(key)
        if len(instances) != 0:
            for inst in instances:

                page.add_text_annot(inst.top_right, bad_words[key])

                highlight = page.add_highlight_annot(inst)
                highlight.set_colors({'stroke': rgb_to_stroke((236, 121, 121)), 'fill': None})
                highlight.update()

document.save(script_path + '/output.pdf')