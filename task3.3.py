import json

with open("RomeoAndJuliet.json", 'r') as f:
    data = json.load(f)
    repl_count = {}
    acts = data["acts"]
    for act in acts:
        scenes = act["scenes"]

        scene_chars = []
        for scene in scenes:
            replics = scene["action"]
            for repl in replics:
                char = repl["character"]
                if char in repl_count:
                    repl_count[char] += 1
                else:
                    repl_count[char] = 1

    max_repls = max(list(repl_count.values()))

    for char, repls in repl_count.items():
        if repls == max_repls:
            print(char)
