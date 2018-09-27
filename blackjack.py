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
        if (self.rank) in ('Валет','Королева','Король','Туз'):
            return 10
        else:
            return ('', 'Туз','2','3','4','5','6','7','8','9','10').index(self.rank)
    def get_rank(self):
        return self.rank

    def __str__(self):
        return "%s%s"  % (self.rank, self. suit)

class BankAccount:
    def __init__(self):
        self.initial_balance = 500
        self.bet = 0
    def moneyOfTheWinner(self, amount):
        self.initial_balance += amount
        return self.initial_balance
    def betOfPlayer(self, playerBet):
        if int(playerBet) > self.initial_balance:
            print("Cумма ставки превышает баланс")
            return self.bet
        if int(playerBet) < self.initial_balance:
            self.initial_balance -= int(playerBet)
            return self.bet
    def moneyOfTheBankAccount(self, amount):
        self.initial_balance -= int(amount)
        return self.initial_balance
    def stateOfAnAccount(self):
        return self.initial_balance

class Deck(object):
    def __init__(self):
        ranks = ('2','3','4','5','6','7','8','9','10','Валет','Королева','Король','Туз')
        suits = ('♦','♥','♣','♠')
        self.cards = [Card(r,s) for r in ranks for s in suits]
        shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()





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

        dct = WorkWithJSON().OpenFile()

        handDict = dct["playerHand"]
        handKeys = list(handDict)
        hand1 = [tuple(handDict[x]) for x in handKeys]

        print(hand1)
    
        for card in hand1:
            print(card)
            result += card.card_value()
            if card.get_rank() == "Туз":
                aces += 1
        if result + aces * 10 <= 21:
            result +=aces * 10
        return result

    def __str__(self):

        if self.name == "Игрок":
            text = "%s содержит :\n" % self.name
            for card in str(GameHistory().playerHand()):
                text += str(card) + " "
            text += "\nЗначение на руке: " + str(self.get_value())
            return text
        if self.name == "Дилер":
            text = "%s содержит :\n" % self.name
            text += "\nЗначение на руке: " + str(self.get_value())
            return text



class Account:
    def __init__(self, id, name_player, balance):
        self.id = id
        self.name = name_player
        self.balance = balance

    def has_id(self,target_id):
        if target_id == self.id:
            return True

    def withdraw(self, amount):
        while amount > self.balance:
            print('Сумма превышает баланс')
            amount = int(input('Пожалуйста введите корректную сумму: \n'))
            continue
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def get_balance(self):
        return self.balance

class BankAccountManager:
    def __init__(self):
        self.account_list = []

    def add_account(self, customer_id, playerName, init_balance):
        self.account_list.append(Account(customer_id, playerName, init_balance))

    def checkID(self, customer_id):
       i = 0
       while i != len(self.account_list):
           if self.account_list[i].has_id(customer_id) == True:
               return i
           else:
               i = i + 1
       raise RuntimeError('No account found!')

    def make_deposit(self, customer_id, amount):
        index = self.checkID(customer_id)
        self.account_list[index].deposit(amount)

    def make_withdrawl(self, customer_id, amount):
        index = self.checkID(customer_id)
#        print index
        self.account_list[index].withdraw(amount)

    def get_balance(self, customer_id):
        index = self.checkID(customer_id)
        self.account_list[index].get_balance()

    def get_account_report(self, customer_id):
        index = self.checkID(customer_id)
        data = (customer_id, self.account_list[index].name, self.account_list[index].get_balance())
        format_string = ("ID: %s\n"
                             "Name: %s\n"
                             "Balance: %.02f\n")
        return format_string % data

class WorkWithJSON:

    def ChangeHandPlayer(self, data):
        dataPlayer = self.OpenFile()

        for key in dataPlayer["playerHand"]:
            if dataPlayer["playerHand"][key] == 0:
                dataPlayer["playerHand"][key] = data
                break

    def OpenFile(self):
        with open('gameHistory.json', 'r') as f:
            data = json.loads(f.read())
            return data

    def WriteFile(self, data):
        with open('gameHistory.json', 'w') as f:
            json.dump(data, f)





class GameHistory:

    def playerHand(self):
        dct = WorkWithJSON().OpenFile()

        return hand

    def jsonName(self):
        dct = WorkWithJSON().OpenFile()
        name = dct["playerData"]["namePlayer"]
        return name
    def editPlayerData(self, id, namePlayer, balancePlayer):
        dct = WorkWithJSON().OpenFile()
        dct["playerData"]["id"] = id
        dct["playerData"]["namePlayer"] = namePlayer
        dct["playerData"]["balancePlayer"] = balancePlayer
        WorkWithJSON().WriteFile(dct)

    def editPlayerWins(self, result):
        dct = WorkWithJSON().OpenFile()
        i = dct["statistics"]["numberOfWins"]
        i = i + result
        dct["statistics"]["numberOfLosers"] = i
        WorkWithJSON().WriteFile(dct)

    def editPlayeLosers(self, result):
        dct = WorkWithJSON().OpenFile()
        i = dct["statistics"]["numberOfLosers"]
        i = i + result
        dct["statistics"]["numberOfLosers"] = i
        WorkWithJSON().WriteFile(dct)
    def stateOfTheBet(self, bet):
        dct = WorkWithJSON().OpenFile()
        dct["bet"] = bet
        WorkWithJSON().WriteFile(dct)
    def getBalance(self):
        dct = WorkWithJSON().OpenFile()
        balance = dct["playerData"]["balancePlayer"]
        return balance
    def new_game(self):
        dct = {"game" : {"state1" : 0, "state2" : 0 ,"state3" : 0, "state4" : 0,
                "state5" : 0, "state6" : 0 ,"state7" : 0, "state8" : 0},
                "playerData" : {"id": None,"namePlayer" : None, "balancePlayer" : None},
                "playerHand": {"1": None , "2" : None, 3 : 0,
                               "4" :0, "5" : 0, "6" : 0,
                               "7" : 0, "8" : 0, "9" : 0},
                "dealerHand" :{"1": [None]},
                "statistics" : {"numberOfWins" : None, "numberOfLosers": None}
               }
        with open('gameHistory.json', 'w+') as file:
            json.dump(dct, file)

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
                    self.runGame()
                break
            if answerToTheQuestion == 2:
                print('Создание нового пользователя:\n')
                answerId = int(input("Введите ID пользователя: "))
                print(answerId)
                answerName = input('Введите имя пользователя: ')
                print(answerName)
                answerInitBalance = int(input('Введите начальный баланс пользователя: '))
                print(answerInitBalance)
                GameHistory().editPlayerData(answerId, answerName, answerInitBalance)

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
    def runGame(self):
        player_hand = Hand("Игрок")
        dealer_hand = Hand("Дилер")

        print("You have " + str(GameHistory().getBalance()) + "$ money")

        GameHistory().stateOfTheBet(int(input("Сделайте ставку \n")))
        d = Deck()
        player_hand.add_card(d.deal_card())
        player_hand.add_card(d.deal_card())

        dealer_hand.add_card(d.deal_card())


        print(dealer_hand)
        print("=" * 20)
        print(player_hand)
if __name__ == "__main__":
    gam = Game()
    gam.new_game()

