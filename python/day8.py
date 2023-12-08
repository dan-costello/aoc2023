import math

# Import and Prep
with open("data/day8.txt") as f:
    data = f.read().split("\n")


def find_lcm_of_list(numbers):
    lcm = numbers[0]
    for i in range(1, len(numbers)):
        gcd = math.gcd(lcm, numbers[i])
        lcm = (lcm * numbers[i]) // gcd
    return lcm


instructions = [i for i in data[0]]

node_dict = {}

for i in data[2:]:
    parts = i.split("=")
    name = parts[0].strip()

    lr = parts[1].split(",")
    left = lr[0][2:]
    right = lr[1][1:-1]
    node_dict[name] = {"L": left, "R": right}


# Part 1
current_node = "AAA"
moves = 0

while current_node != "ZZZ":
    for i in instructions:
        current_node = node_dict[current_node][i]
        moves += 1
        if current_node == "ZZZ":
            break

print("Part 1: ", moves)

# Part 2
a_nodes = [a for a in node_dict.keys() if a.endswith("A")]
moves = 0


movecounts = []
for node in a_nodes:
    moves = 0
    current_node = node
    while not current_node.endswith("Z"):
        for i in instructions:
            current_node = node_dict[current_node][i]
            moves += 1
            if current_node.endswith("Z"):
                break
    movecounts.append(moves)

print("Part 2: ", find_lcm_of_list(movecounts))
