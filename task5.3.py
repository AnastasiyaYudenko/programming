import collections
import json

with open('RomeoAndJuliet.json', 'r', encoding='utf-8') as s:
    data = json.load(s)
    counter = collections.Counter()
    repl_count = []
    acts = data["acts"]
    for act in acts:
        scenes = act["scenes"]

        for scene in scenes:
            replics = scene["action"]
            for repl in replics:
                repl_count.append(repl["character"])

    counter_repl = list(dict(collections.Counter(repl_count)).items())

    sorted_repls = sorted(counter_repl, key=lambda character: character[1], reverse=True)
print(sorted_repls)
