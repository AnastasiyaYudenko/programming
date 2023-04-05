import json

characters = []
with open('RomeoAndJuliet.json', 'r') as s:
    data = json.load(s)
    acts = data["acts"]
    for act in acts:
        scenes = act["scenes"]

        scene_chars = set()
        for scene in scenes:
            replics = scene["action"]
            for repl in replics:
                chars = repl["character"]
                scene_chars.add(chars)

            characters.append(list(scene_chars))

print(characters)
with open('charac.json', 'w') as a:

    to_write = []
    for line in characters:
        a.write(json.dumps(line))
        a.write('\n')
