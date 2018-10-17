class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def card_value(self):
        if self.rank in ('Валет', 'Королева', 'Король'):
            return 10
        elif self.rank in 'Туз':
            return 11
        else:
            return ('', 'Туз', '2', '3', '4', '5', '6', '7', '8', '9', '10').index(self.rank)

    def get_rank(self):
        return self.rank

    def __str__(self):
        return "%s%s" % (self.rank, self.suit)
