from collections import Counter

with open("data/day7.txt") as f:
    data = f.read().split("\n")

card_strength = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
j_card_strength = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]


def get_winnings(hands):
    ranked = sorted(hands, key=lambda x: (x.counts, x.cardstrength))
    return sum([h.bid * (i + 1) for i, h in enumerate(ranked)])


class Hand:
    def __init__(self, card):
        self.card = card.split(" ")[0]
        self.bid = int(card.split(" ")[1])
        self.cardstrength = [card_strength.index(i) for i in card.split(" ")[0]]
        self.counts = sorted(list(Counter(card.split(" ")[0]).values()), reverse=True)
        self.countdict = dict(
            sorted(
                dict(Counter(self.cardstrength)).items(),
                key=lambda item: item[0],
                reverse=True,
            )
        )

    def convert_jokers(self):
        sorted_dict = dict(
            sorted(self.countdict.items(), key=lambda item: item[1], reverse=True)
        )
        # handle edge case of all jokers
        if sorted_dict == {9: 5}:
            sorted_dict = {12: 5}
        max_card = [i for i in sorted_dict.keys() if i != 9][0]
        jokers = self.countdict.get(9)
        if jokers and sorted_dict != {12: 5}:
            self.countdict[max_card] = self.countdict[max_card] + jokers
            del self.countdict[9]
            self.counts = sorted([i for i in self.countdict.values()], reverse=True)
        self.cardstrength = [j_card_strength.index(i) for i in self.card.split(" ")[0]]


# Part 1
print("Part 1", get_winnings([Hand(i) for i in data]))


# Part 2
new_hands = []
for i in data:
    h = Hand(i)
    h.convert_jokers()
    new_hands.append(h)

print("Part 2", get_winnings(new_hands))
