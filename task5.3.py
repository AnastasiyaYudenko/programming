import collections
import json

with open('RomeoAndJuliet.json', 'r', encoding='utf-8') as s:
    data = json.load(s)
    counter = collections.Counter()
    acts = data["acts"]
    for act in acts:
        scenes = act["scenes"]

        for scene in scenes:
            replics = scene["action"]
            for repl in replics:
                counter[repl["character"]] += 1

print(counter)
