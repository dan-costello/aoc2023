import re
from functools import reduce
from collections import defaultdict
import operator

with open("data/day3.txt") as f:
    data = f.read().splitlines()


def find_numbers(input):
    matches = re.finditer(r"\b\d+\b", input)
    return [
        (int(match.group()), match.start(), match.start() + len(match.group()))
        for match in matches
    ]


# Unique list of all symbols
symbols = list(
    set([char for line in data for char in line if not char.isdigit() and char != "."])
)

# to avoid indexing problems I am adding a line of periods to start
# and a period to start and end of each line
empty_line = "." * len(data[0])
data.insert(0, empty_line)
data.append(empty_line)
data = ["." + line + "." for line in data]


# Part 1
valid_parts = []
for index, line in enumerate(data):
    numbers = find_numbers(line)
    for num in numbers:
        value, start, end = num
        # each time a valid number is found,
        # search surrounding values for a symbol
        prev = data[index - 1][start - 1 : end + 1]
        line = data[index + 0][start - 1 : end + 1]
        next = data[index + 1][start - 1 : end + 1]
        all = prev + line + next
        if any(symbol in all for symbol in symbols):
            valid_parts.append(value)

print("Part 1: ", sum(valid_parts))

# Part 2
potential_gears = []
for index, line in enumerate(data):
    numbers = find_numbers(line)
    for num in numbers:
        value, start, end = num
        # if star is found adjacent to number, log the number value and star index to compare with others
        prev = data[index - 1][start - 1 : end + 1]
        if "*" in prev:
            potential_gears.append((value, (index - 1, start - 1 + prev.index("*"))))
        line = data[index + 0][start - 1 : end + 1]
        if "*" in line:
            potential_gears.append((value, (index + 0, start - 1 + line.index("*"))))
        next = data[index + 1][start - 1 : end + 1]
        if "*" in next:
            potential_gears.append((value, (index + 1, start - 1 + next.index("*"))))


# create dict of stars/gears with index as key and adjacent parts as list
gear_dict = defaultdict(list)
for val, indices in potential_gears:
    gear_dict[indices].append(val)

# multiply together part numbers if part of length-2 array
two_part_gears = [reduce(operator.mul, i) for i in gear_dict.values() if len(i) == 2]
print("Part 2: ", sum(two_part_gears))
