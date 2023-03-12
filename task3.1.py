import json

words = {}

with open('wikidata_1000.json', 'r', encoding='utf8') as f:
    for line in f:
        data = json.loads(line)
        word = data["label"]["value"]
        if "description" in data:
            d = data["description"]["value"]
        else:
            d = None
        words[word] = d


with open('words.json', 'w') as a:
    json.dump(words, a, ensure_ascii=False, indent=4)
