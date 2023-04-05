from collections import defaultdict
import json

with open('RomeoAndJuliet.json', 'r', encoding='utf-8') as a:
    data = json.load(a)
    acts = data["acts"]
    d = defaultdict(list)

    for act in acts:
        scenes = act["scenes"]
        for scene in scenes:
            action = scene["action"]
            for act in action:
                replics = act["says"]
                char = act["character"]
                d[char].extend(replics)
    print(d)





