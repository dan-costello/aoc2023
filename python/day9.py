import numpy as np

# Import and Prep
with open("data/day9.txt") as f:
    data = [[int(i) for i in line.split()] for line in f.read().split("\n")]


def find_last(lst):
    return 0 if all(x == 0 for x in lst) else lst[-1] + find_last(np.diff(lst))


part1 = sum([find_last(l) for l in data])
print("Part 1: ", part1)


part2 = sum([find_last(l[::-1]) for l in data])
print("Part 2: ", part2)
