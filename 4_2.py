import xml.etree.ElementTree as et
tree = et.parse('annot.opcorpora.no_ambig.xml')
root = tree.getroot()

nouns = []


for token in root.iter('token'):
    gs = []
    for g in token.iter("g"):
        gs.append(g.attrib["v"])
    if "NOUN" in gs and "plur" in gs:
        nouns.append(token.attrib['text'])


with open('ns.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(nouns))