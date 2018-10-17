from random import shuffle
from Card import *


class Deck(object):
    def __init__(self):
        ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Валет', 'Королева', 'Король', 'Туз')
        suits = ('♦', '♥', '♣', '♠')
        self.cards = [Card(r, s) for r in ranks for s in suits]
        shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()
