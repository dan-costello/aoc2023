import re
from functools import reduce
from collections import defaultdict
import operator


# Data prep and helper functions
with open("data/day3.txt") as f:
    data = f.read().splitlines()


def find_numbers(input):
    matches = re.finditer(r"\b\d+\b", input)
    return [
        (int(match.group()), match.start(), match.start() + len(match.group()))
        for match in matches
    ]


# to avoid indexing problems I am adding a line of periods to start
# and a period to start and end of each line
empty_line = "." * len(data[0])
data.insert(0, empty_line)
data.append(empty_line)
data = ["." + line + "." for line in data]


# Part 1

# Unique list of all symbols
symbols = list(
    set([char for line in data for char in line if not char.isdigit() and char != "."])
)


valid_parts = []
for index, line in enumerate(data):
    numbers = find_numbers(line)
    for num in numbers:
        value, start, end = num
        # build string of surrounding chars
        all = ""
        for offset in [-1, 0, 1]:
            all += data[index + offset][start - 1 : end + 1]
        if any(symbol in all for symbol in symbols):
            valid_parts.append(value)

print("Part 1: ", sum(valid_parts))

# Part 2
gear_dict = defaultdict(list)
for index, line in enumerate(data):
    numbers = find_numbers(line)
    for num in numbers:
        value, start, end = num
        # if star is found adjacent to number, log the number value and star index to compare with others
        for offset in [-1, 0, 1]:
            line = data[index + offset][start - 1 : end + 1]
            if "*" in line:
                indices = (index + offset, start - 1 + line.index("*"))
                gear_dict[indices].append(value)

# multiply together part numbers if part of length-2 array
two_part_gears = [reduce(operator.mul, i) for i in gear_dict.values() if len(i) == 2]
print("Part 2: ", sum(two_part_gears))
