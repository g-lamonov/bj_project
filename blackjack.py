#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8
import json
from random import shuffle
class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def card_value(self):
        if self.rank in ('Валет','Королева','Король','Туз'):
            return 10
        else:
            return ('', 'Туз','2','3','4','5','6','7','8','9','10').index(self.rank)
    def get_rank(self):
        return self.rank

    def __str__(self):
        return "%s%s"  % (self.rank, self. suit)

class Deck(object):
    def __init__(self):
        ranks = ('2','3','4','5','6','7','8','9','10','Валет','Королева','Король','Туз')
        suits = ('♦','♥','♣','♠')
        self.cards = [Card(r,s) for r in ranks for s in suits]
        shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

class WorkWithJSON:

    def ChangeHandPlayer(self, data):
        dataPlayer = self.OpenFile()

        for key in dataPlayer["action2"]["playerHand"]:
            if dataPlayer["action2"]["playerHand"][key] == 0:
                dataPlayer["action2"]["playerHand"][key] = data
                break

    def OpenFile(self):
        with open('gameHistory.json', 'r') as f:
            data = json.loads(f.read())
            return data

    def WriteFile(self, data):
        with open('gameHistory.json', 'w') as f:
            json.dump(data, f)



class Hand(object):
    def __init__(self, name):
        self.name = name
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)
        WorkWithJSON().ChangeHandPlayer(card)


    def get_value(self):
        result = 0
        aces = 0
        for card in self.cards:
            result += card.card_value()
            if card.get_rank() == "Туз":
                aces += 1
        if result + aces * 10 <= 21:
            result +=aces * 10
        return result

    def __str__(self):
        text = "%sсодержит :\n" % self.name
        for card in self.cards:
            text += str(card) + " "
        text += "\nЗначение на руке: " + str(self.get_value())

        return text



class GameHistory:
    def __init__(self):
        self.dct = {"game": {"state1": "0", "state2": "0", "state3": "0", "state4": "0"},
                    "action1": {"id": "id", "namePlayer": "Petya", "balancePlayer": "balance"},
                       "action2": {"playerHand": {"1": ["2", "\u2665"], "2": ["7", "\u2663"]}},
                       "action3": {"dealerHand": {"1": ["3", "\u2664"]}}}

    def jsonName(self):
        return self.dct["action1"]["namePlayer"]

    def new_game():
        dct = {"game" : {"state1" : 0, "state2" : 0 ,"state3" : 0, "state4" : 0,
                "state5" : 0, "state6" : 0 ,"state7" : 0, "state8" : 0},
                "playerData" : {"id": None,"namePlayer" : None, "balancePlayer" : None},
                "action2" : {"playerHand": {"1": None , "2" : None, 3 : 0,
                               "4" :0, "5" : 0, "6" : 0,
                               "7" : 0, "8" : 0, "9" : 0}},
                "action3" : {"dealerHand" :{"1": [None]}},
                "statistics" : {"numberOfWins" : 15, "numberOfLosers": 10}
               }

class Game():

    def new_game(self):
        reading = WorkWithJSON()
        data = reading.OpenFile()
        for key in data["game"]:
            if data["game"][key] == 1:
                query = input("Желаете продолжить игру с прошлого момента? (y/n) \n")
                if query == 'y':
                    if data["game"]["state1"] == 1:
                        self.Bet()
                    if data["game"]["state2"] == 1:
                        pass
                    if data["game"]["state3"] == 1:
                        pass

                if query == 'n':
                    self.Authorization()
        self.Authorization()


    def Authorization(self):
        reading = WorkWithJSON()
        data = reading.OpenFile()

        while True:
            answerToTheQuestion = int(input(
                "Добро пожаловать, выберите пользователя:\n1 Продолжить игру"
                "\n2 Создать нового пользователя\n3 Вывести статистику игрока \nВвод: "))

            if answerToTheQuestion == 1:
                with open('gameHistory.json', 'r') as f:
                    playerData = (data["playerData"]["id"],
                                  data["playerData"]["namePlayer"],
                                  data["playerData"]["balancePlayer"])
                    print(playerData)
                break
            if answerToTheQuestion == 2:
                print('Создание нового пользователя:\n')
                answerId = int(input("Введите ID пользователя: "))
                print(answerId)
                answerName = input('Введите имя пользователя: ')
                print(answerName)
                answerInitBalance = int(input('Введите начальный баланс пользователя: '))
                print(answerInitBalance)

                continue

            if answerToTheQuestion == 3:
                with open('gameHistory.json', 'r') as f:
                    data = json.loads(f.read())

                    userInformation = (data["playerData"]["id"],
                                       data["playerData"]["namePlayer"],
                                       data["playerData"]["balancePlayer"],
                                       data["statistics"]["numberOfWins"],
                                       data["statistics"]["numberOfLosers"])
                    templateForTheUser = ("ID: %s\n"
                                          "Имя: %s\n"
                                          "Баланс: %d\n"
                                          "Количество побед: %d\n"
                                          "Количество проигршей: %d\n")
                    print(templateForTheUser % userInformation)
                continue
    def Bet(self):
        print("i'm here")

if __name__ == "__main__":
    gam = Game()
    gam.new_game()

