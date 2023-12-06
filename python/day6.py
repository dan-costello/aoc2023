from functools import reduce
import operator

with open("data/day6.txt") as f:
    data = f.read().split("\n")

# Part 1
data = [i.split(":")[1] for i in data[:2]]
data = [j.split(" ") for j in data]
time = [int(i) for i in data[0] if i.isdigit()]
distance = [int(i) for i in data[1] if i.isdigit()]

mapped = set(zip(time, distance))
ways = [
    len([i for i in range(time) if (time - i) * i > record]) for time, record in mapped
]

print("Part 1: ", reduce(operator.mul, ways))


# Part 2
time_big = [int("".join([str(i) for i in time]))]
distance_big = [int("".join([str(i) for i in distance]))]
mapped_big = set(zip(time_big, distance_big))

ways_big = [
    len([i for i in range(time) if (time - i) * i > record])
    for time, record in mapped_big
][0]

print("Part 2: ", ways)
