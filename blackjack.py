
class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.rank = rank

    def show(self):
        print "{} of {}".format(self.value, self.suit)

    def card_value(self):
        if self.rank in "TJQK":
            return 10
        else:
            return "A23456789".index(self.rank)

class Hand(object):
    def __init__(self, name):
        self.name = name
        self.cards = []                 # в руке ничего
    def add_card(self, card):
        self.cards.append(card)
        result = 0
        aces = 0
        for card in self.cards:
            result += card.card_value()
            if card.get_rank() = "A":
                aces += 1
        if result + aces*10 <= 21:
            result += aces*10
        return result

    def __str__(self):

class Deck(object):
    def __init__(self):
        self.cards = [Card(r,s) for r in ranks for s in suits]



    def build(self):
        for sui in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for valu in range(1, 14):
                print "{} of {}".format(valu, sui)

class new_game():




deck = Deck()
