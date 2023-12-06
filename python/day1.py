with open("data/day1.txt") as f:
    data = f.read().splitlines()

# Part 1
nums = [[d for d in list(i) if d.isdigit()] for i in data]
fl = [int(l[0] + l[-1]) for l in nums]

print("Part 1: ", sum(fl))

# Part 2

str_to_int = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}
filter = []


def find_all(input_string, substring):
    start = 0
    while True:
        start = input_string.find(substring, start)
        if start == -1:
            return
        yield start
        start += len(substring)


for i in data:
    locs = {}
    for j in str_to_int.keys():
        matches = list(find_all(i, j))
        for index in matches:
            locs[index] = j
    if len(locs) > 0:
        sort = dict(sorted(locs.items()))
        map = [str_to_int[j] for j in [sort[i] for i in sort]]
        filter.append(int(str(map[0]) + str(map[-1])))
print("Part 2: ", sum(filter))
