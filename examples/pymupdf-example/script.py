import fitz, os, argparse

bad_words = {
    'Parent': "parent(s)/guardian",
    'Mother/Father': "parent(s)/Guardian", 
    ' sex ': "gender assigned at birth",
    'spouse': 'partner(s)',
    'son/daughter': 'child', 
    'marital status': 'relationship status',
    'Preferred name': 'chosen name', 
}
missing_words = {
    'sexuality': ['sexuality', 'sexual orientation', 'sexual preference'],
    'honorifics': ['Mr.', 'Mrs.', 'Title', 'Position', 'Prefix'],
    'prefname': ['Preferred name', 'Chosen name'],
    'pronouns': ['Pronouns'],
    #'bogus': ['bogus'],
    #'Hot chocolate': ['Hot chocolate', 'Hot cocoa'],
}
missing_comments = {
    'honorifics': 'Consider adding an honorific/title field',
    "sexuality": "Consider adding a section for patients to add their sexuality if they wish",
    'prefname': 'Consider adding a "chosen name" field',
    'pronouns': 'Consider adding a pronouns field',
    #'bogus': 'this missing word is bogus.',
    #'Hot chocolate': 'How dare you not have hot chocolate in your form',
}

def rgb_to_stroke(rgb):
    return tuple([x / 255 for x in rgb])

def lint_pdf(infile: str, outfile: str):
    document = fitz.open(infile)
    missing_words_count = { k: 0 for k in missing_words.keys() }

    for page in document:
        for word, better_word in bad_words.items():
            instances = page.search_for(word)
            for inst in instances:
                comment = 'Consider changing {0} to {1}.'.format(word, better_word)
                page.add_text_annot(inst.top_right, comment)
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
    document.save(outfile)

def main():
    parser = argparse.ArgumentParser(
        prog='FormThisWayLinter',
        description='Linter for healthcare forms to use \
            inclusive language and data collection',
    )
    parser.add_argument('infile')
    parser.add_argument('outfile', nargs='?', default='output.pdf')
    args = parser.parse_args()
    lint_pdf(args.infile, args.outfile)
    print('Successfully linted and outputted to {0}'.format(args.outfile))

if __name__ == '__main__':
    main()