
class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print "{} of {}".format(self.value, self.suit)



class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for sui in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for valu in range(1, 14):
                print "{} of {}".format(valu, sui)



deck = Deck()
