import json

characters = []
with open('RomeoAndJuliet.json', 'r') as s:
    data = json.load(s)
    acts = data["acts"]
    for act in acts:
        scenes = act["scenes"]

        scene_chars = []
        for scene in scenes:
            replics = scene["action"]
            for repl in replics:
                chars = repl["character"]
                scene_chars.append(chars)

            characters.append(list(set(scene_chars)))

print(characters)
with open('charac.json', 'w') as a:
    to_write = []
    for line in characters:
        to_write.append(json.dumps(', '.join(line)))
    json.dump(to_write, a, ensure_ascii=False, indent=4)