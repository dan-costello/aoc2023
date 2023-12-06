# Data prep and helper functions
with open("data/day5.txt") as f:
    data = f.read().split("\n\n")

map_names = [i.split(":")[0].replace(" map", "") for i in data]
map_instructions = {map_names[i]: data[i].split("\n")[1:] for i in range(1, 8)}


class plantMap:
    def __init__(self, dest_start, source_start, range):
        self.dest_start = int(dest_start)
        self.source_start = int(source_start)
        self.range = int(range)
        self.source_end = self.source_start + self.range
        self.dest_end = self.dest_start + self.range
        self.diff = self.dest_start - self.source_start

    def __repr__(self):
        return f"Start:{self.source_start}, End:{self.source_end} Range:{self.range}"


plant_mappings = {}
for mapname, mapvalues in map_instructions.items():
    plant_mappings[mapname] = []
    for seedmap in mapvalues:
        dest_start, source_start, map_range = [int(i) for i in seedmap.split(" ")]
        plant_mappings[mapname].append(plantMap(dest_start, source_start, map_range))

# Part 1

seeds = [int(i) for i in data[0].split(":")[1].split(" ") if i.isdigit()]
loc_numbers = []
for i in seeds:
    val = i
    for mapping in map_names[1:]:
        mps = plant_mappings[mapping]
        changed = False
        for mp in mps:
            if (mp.source_start <= val <= mp.source_end) and not changed:
                val = val + mp.diff
                changed = True

    loc_numbers.append(val)

print("Part 1", min(loc_numbers))

# Part 2

seed_maps = [[v, v + seeds[i + 1]] for i, v in enumerate(seeds) if i % 2 == 0]
seed_start = min([i[0] for i in seed_maps])
min_location = min(loc_numbers)
for i in range(seed_start, min_location):
    val = i
    for mapping in map_names[-1:0:-1]:
        mps = plant_mappings[mapping]
        checks = [(mp.dest_start <= val <= mp.dest_end) for mp in mps]
        if any(checks):
            corr = [i for i, val in enumerate(checks) if val == True][0]
            val = val - mps[corr].diff
    for seed_start, seed_end in seed_maps:
        if seed_start <= val <= seed_end:
            print("Part 2: ", i)
            exit()
