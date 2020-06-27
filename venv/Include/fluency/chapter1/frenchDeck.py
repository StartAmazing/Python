import collections

# namedtuple 用于构建只有少数属性但是没有方法的对象
Card = collections.namedtuple('Card', ['rank', 'suit'])
beer_card = Card('7', 'diamonds')
print(beer_card)

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

deck = FrenchDeck()
print(len(deck))
print(deck[0])
print(deck[-1])

from random import choice
print(choice(deck))
print(choice(deck))
print(choice(deck))

print("------------------- slice ----------------------")
print(deck[:3])

print(deck[12::13])

for card in deck:
    print(card, end="\t")
print()
for card in reversed(deck):
    print(card, end="\t")
print()

print("---------------------- in ---------------------")
card1 = Card('Q', 'hearts')
card2 = Card('Q', 'beats')
print(card1 in deck)
print(card2 in deck)

print("----------------------- sort ------------------")
suit_values = dict(spades=3, hearts =2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high, reverse=True):
    print(card, end="\t")
