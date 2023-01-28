import fitz, os

def rgb_to_stroke(rgb):
    return tuple([x / 255 for x in rgb])

script_path = os.path.dirname(os.path.realpath(__file__))
document = fitz.open(script_path + '/../inputs/intake1.pdf')
bad_words = {
    'Parent': "parent(s)/guardian",
    'Mother/Father': "parent(s)/Guardian", 
    ' sex ': "gender assigned at birth",
    'spouse': 'partner(s)',
    'son/daughter': 'child', 
    'name': 'legal name and chosen name',
    'marital status': 'relationship status',
}
missing_words = {
    "sexuality": ["sexuality", 'sexual orientation', 'sexual preference'],
    'honorifics': ['Mr.', 'Mrs.', 'Title', 'Position', 'Prefix'],
    #'bogus': ['bogus'],
    #'Hot chocolate': ['Hot chocolate', 'Hot cocoa'],
}
missing_comments = {
    'honorifics': 'Add an honorific bruh',
    "sexuality": "consider adding a section for patients to add their sexuality if they wish.",
    #'bogus': 'this missing word is bogus.',
    #'Hot chocolate': 'How dare you not have hot chocolate in your form',
}
missing_words_count = { k: 0 for k in missing_words.keys() }

for page in document:
    for key in bad_words.keys():
        instances = page.search_for(key)
        for inst in instances:
            page.add_text_annot(inst.top_right, bad_words[key])

            highlight = page.add_highlight_annot(inst)
            highlight.set_colors({'stroke': rgb_to_stroke((255, 108, 79)), 'fill': None})
            highlight.update()
    
    for category, wordlist in missing_words.items():
        for word in wordlist:
            instances = page.search_for(word)
            missing_words_count[category] += len(instances)

annotation_comments = []
for category, count in missing_words_count.items():
    if count == 0:
        annotation_comments.append(missing_comments[category])

if len(annotation_comments) != 0:
    document[0].add_text_annot((15, 15), '\n\n'.join(annotation_comments))

document.save(script_path + '/output.pdf')