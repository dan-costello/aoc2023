# Data prep and helper functions
with open("data/day4.txt") as f:
    data = f.read().splitlines()

# Part 1
point_count = 0
for i in data:
    numbers = i.split(":")[1].strip().split(" | ")
    winning = [int(i.strip()) for i in numbers[0].split(" ") if i.isdigit()]
    mine = [int(i) for i in numbers[1].split(" ") if i.isdigit()]
    matches = [i for i in winning if i in mine]
    if matches:
        point_count += 2 ** (len(matches) - 1)

print("Part 1: ", point_count)

# Part 2
card_counts = [1 for i in data]
point_count = 0
for i, count in enumerate(card_counts):
    for c in range(count):
        numbers = data[i].split(":")[1].strip().split(" | ")
        winning = [int(i.strip()) for i in numbers[0].split(" ") if i.isdigit()]
        mine = [int(i) for i in numbers[1].split(" ") if i.isdigit()]
        matches = [i for i in winning if i in mine]
        if matches:
            for m in range(1, len(matches) + 1):
                card_counts[m + i] += 1

print("Part 2: ", sum(card_counts))
