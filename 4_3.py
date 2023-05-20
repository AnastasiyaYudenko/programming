import xml.etree.ElementTree as et
tree = et.parse('annot.opcorpora.no_ambig.xml')
root = tree.getroot()

how_many = {"VERB": 0, "CONJ": 0}

for token in root.iter('token'):
    if token.attrib["text"].lower() == 'может':
        gs = []
        for g in token.iter("g"):
            gs.append(g.attrib["v"])
        if "VERB" in gs:
            how_many["VERB"] += 1
        elif "CONJ" in gs:
            how_many["CONJ"] += 1

print(how_many)

