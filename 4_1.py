import xml.etree.ElementTree as et
tree = et.parse('annot.opcorpora.no_ambig.xml')
root = tree.getroot()

sent = []
for source in root.iter('source'):
    sent.append(source.text)

with open("sentt.txt", 'w', encoding='utf-8') as f:
    f.write('\n'.join(sent))

