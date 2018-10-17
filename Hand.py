from GameHistory import *


class Hand(object):
    def __init__(self, name):
        self.name = name
        self.cards = []

    def add_card(self, card):
        while True:
            if self.name == "Игрок":
                history = GameHistory()
                self.cards = []
                self.cards.append(card)
                dct = WorkWithJson().open_file()
                lis_player_hand = dct["player_hand"]
                dct["player_points"] = self.get_value()
                lis_player_hand.append(str(card))
                WorkWithJson.write_file(dct)
                history.change_hand_player(lis_player_hand)
                break
            if self.name == "Дилер":
                history = GameHistory()
                self.cards = []
                self.cards.append(card)
                dct = WorkWithJson().open_file()
                lis = dct["dealer_hand"]
                lis.append(str(card))

                dct["dealer_points"] = self.get_value()
                WorkWithJson.write_file(dct)
                history.change_dealer_player(lis)

                break
            break

    def get_value(self):

        if self.name == "Игрок":
            card = self.cards[0]
            points = GameHistory().get_player_points()
            points += card.card_value()
            return points

        if self.name == "Дилер":
            for card in self.cards:
                points = GameHistory().get_dealer_points()
                points += card.card_value()

                return points

    def __str__(self):

        if self.name == "Игрок":
            text = "%s содержит :\n" % self.name
            for card in (GameHistory().player_hand()):
                text += str(card) + " "
            text += "\nЗначение на руке: " + str(GameHistory().get_player_points())
            return text
        if self.name == "Дилер":
            text = "%s содержит :\n" % self.name
            for card in (GameHistory().dealer_hand()):
                text += str(card) + " "
            text += "\nЗначение на руке: " + str(GameHistory().get_dealer_points())
            return text
