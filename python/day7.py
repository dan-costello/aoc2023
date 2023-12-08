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
        self.card, bid = card.split(" ")
        self.bid = int(bid)
        self.card_list = [i for i in self.card]
        self.cardstrength = [card_strength.index(i) for i in self.card_list]
        self.countdict = {
            k: v for k, v in sorted(Counter(self.cardstrength).items(), reverse=True)
        }
        self.counts = sorted(self.countdict.values(), reverse=True)

    def convert_jokers(self):
        sorted_dict = dict(
            sorted(self.countdict.items(), key=lambda item: item[1], reverse=True)
        )
        if sorted_dict == {9: 5}:
            sorted_dict = {12: 5}
        max_card = next(i for i in sorted_dict.keys() if i != 9)
        jokers = self.countdict.get(9)
        if jokers and sorted_dict != {12: 5}:
            self.countdict[max_card] += jokers
            del self.countdict[9]
        self.counts = sorted(self.countdict.values(), reverse=True)
        self.cardstrength = [j_card_strength.index(i) for i in self.card_list]


# Part 1
print("Part 1", get_winnings([Hand(i) for i in data]))


# Part 2
new_hands = []
for i in data:
    h = Hand(i)
    h.convert_jokers()
    new_hands.append(h)

print("Part 2", get_winnings(new_hands))
