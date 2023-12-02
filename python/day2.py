from functools import reduce
import operator

with open("data/day2.txt") as f:
    data = f.read().splitlines()
    data = {i.split(":")[0]: i.split(":")[1] for i in data}

new_data = {}
for k, v in data.items():
    all_trials = []

    all_items = v.split(";")
    for oneroll in all_items:
        new_dict = {}
        details = oneroll.strip().split(",")
        for colorcount in details:
            final = colorcount.strip().split(" ")
            new_dict[final[1]] = int(final[0])
        all_trials.append(new_dict)
    new_data[int(k.split(" ")[1])] = all_trials

test = {"red": 12, "green": 13, "blue": 14}

# Part 1:
max_values = {}
for k, v in new_data.items():
    max_colors = {"red": 0, "green": 0, "blue": 0}
    for roll in v:
        for color, count in roll.items():
            max_colors[color] = max(max_colors[color], count)
    max_values[k] = max_colors


possible_games = [
    k
    for k, v in max_values.items()
    if all(v[color] <= test[color] for color in test.keys())
]

print("Part 1: ", sum(possible_games))

# Part 2
products = [reduce(operator.mul, list(v.values())) for v in max_values.values()]
print("Part 2: ", sum(products))
