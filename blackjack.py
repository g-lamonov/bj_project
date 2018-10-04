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
        return "%s%s" % (self.rank, self. suit)

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
        self.cards = [Card(r,s)for r in ranks for s in suits]
        shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

class Hand(object):
    def __init__(self, name):
        self.name = name
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)
        print(card)
        dct = WorkWithJSON().OpenFile()
        while True:
            if self.name == "Игрок":
                lis = dct["playerHand"]
                print(lis)
                lis.append(str(card))
                print(lis)
                break
            if self.name == "Дилер":
                lis = dct["dealerHand"]
                print(lis)
                lis.append(str(card))
                print(lis)
                break

        if self.name == "Игрок":
            GameHistory().ChangeHandPlayer(lis)

        if self.name == "Дилер":
            GameHistory().ChangeDealerPlayer(lis)


    def get_value(self):
        result = 0
        aces = 0

        for card in self.cards:
            result += card.card_value()
            if card.get_rank() == "Туз":
                aces += 1
        if result + aces * 10 <= 21:
            result += aces * 10

        return result


    def __str__(self):

        if self.name == "Игрок":
            text = "%s содержит :\n" % self.name
            for card in (GameHistory().playerHand()):
                text += str(card) + " "
            text += "\nЗначение на руке: " + str(self.get_value())
            return text
        if self.name == "Дилер":
            text = "%s содержит :\n" % self.name
            for card in (GameHistory().dealerHand()):
                text += str(card) + " "
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

    def OpenFile(self):
        with open('gameHistory.json', 'r') as f:
            data = json.loads(f.read())
            return data

    def WriteFile(self, data):
        with open('gameHistory.json', 'w') as f:
            json.dump(data, f)


class GameHistory:
    def ChangeHandPlayer(self, data):
        dct = WorkWithJSON().OpenFile()
        dct["playerHand"] = data
        WorkWithJSON().WriteFile(dct)

    def ChangeDealerPlayer(self, data):
        dct = WorkWithJSON().OpenFile()
        dct["dealerHand"] = data
        WorkWithJSON().WriteFile(dct)

    def playerHand(self):
        dct = WorkWithJSON().OpenFile()
        handP = dct["playerHand"]

        return handP

    def dealerHand(self):
        dct = WorkWithJSON().OpenFile()
        handP = dct["dealerHand"]

        return handP

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
    def get_player_points(self):
        dct = WorkWithJSON().OpenFile()
        points = dct["player_points"]
        return points

    def change_player_points(self, data):
        dct = WorkWithJSON().OpenFile()
        dct["player_points"] = data
        WorkWithJSON().WriteFile(dct)

    def get_dealer_points(self):
        dct = WorkWithJSON().OpenFile()
        points = dct["dealer_points"]
        return points

    def change_dealer_points(self, data):
        dct = WorkWithJSON().OpenFile()
        dct["dealer_points"] = data
        WorkWithJSON().WriteFile(dct)

    def new_game(self):
        dct = {"game" : {"state1" : 0, "state2" : 0 ,"state3" : 0, "state4" : 0,
                "state5" : 0, "state6" : 0 ,"state7" : 0, "state8" : 0},
                "playerData": {"id": None,"namePlayer" : None, "balancePlayer" : None},
                "playerHand": [],
                "dealerHand": [],
                "statistics": {"numberOfWins" : None, "numberOfLosers": None}
               }
        with open('gameHistory.json', 'w+') as file:
            json.dump(dct, file)
    def add_card1(self, card):
        dct = WorkWithJSON().OpenFile()
        cardItems = list(dct["playerHand"])
        cardItems.append(card)
        dct["playerHand"] = cardItems
        WorkWithJSON().WriteFile(dct)



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

                playerData = (data["playerData"]["id"],
                              data["playerData"]["namePlayer"],
                              data["playerData"]["balancePlayer"])
                print(playerData)
                dct = WorkWithJSON().OpenFile()
                dct["playerHand"] = []
                dct["dealerHand"] = []
                dct["player_points"] = 0
                dct["dealer_points"] = 0
                WorkWithJSON().WriteFile(dct)
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
                                          "Количество проигрышей: %d\n")
                    print(templateForTheUser % userInformation)
                continue
    def runGame(self):
        reading = WorkWithJSON()
        data = reading.OpenFile()

        player_hand = Hand("Игрок")
        dealer_hand = Hand("Дилер")

        print("You have " + str(GameHistory().getBalance()) + "$ money")

        GameHistory().stateOfTheBet(int(input("Сделайте ставку \n")))
        d = Deck()

        player_hand.add_card(d.deal_card())
        points = player_hand.get_value()
        GameHistory().change_player_points(points)

        player_hand.add_card(d.deal_card())
        points = player_hand.get_value()
        GameHistory().change_player_points(points)

        dealer_hand.add_card(d.deal_card())
        points = dealer_hand.get_value()
        GameHistory().change_dealer_points(points)

        print(dealer_hand)
        print("=" * 20)
        print(player_hand)

        in_game = True
        print(GameHistory().get_player_points())
        while player_hand.get_value() < 21:
            while True:
                print(GameHistory().get_player_points())
                query = input("Идти дальше? (y/n) \n")
                ans = query[0].lower()
                if query == '' or not ans in ['y', 'n']:
                    print('Пожалуйста ответьте y или n!')
                else:
                    break

            if ans == "y":
                player_hand.add_card(d.deal_card())
                print(player_hand)
                points = player_hand.get_value()
                GameHistory().change_player_points(points)
                if points > 21:
                    print("Ты проиграл")
                    print("-*" * 10 + "-")
                    print("Твой баланс был: " + str(data["playerData"]["balancePlayer"]))
                    data["playerData"]["balancePlayer"] = data["playerData"]["balancePlayer"] - data["bet"]
                    print("Твой баланс стал: " + str(data["playerData"]["balancePlayer"]))
                    print("-*" * 10 + "-")
                    WorkWithJSON().WriteFile(data)
                    in_game = False
                else:
                    print("Ты стоишь!")
                    break

        print("=" * 20)
        if in_game:
            while GameHistory().get_dealer_points() < 17:
                dealer_hand.add_card(d.deal_card())
                print(dealer_hand)
                if GameHistory().get_dealer_points() > 21:
                    print("Дилер проиграл")
                    print("-*" * 10 + "-")
                    print("Твой баланс был: " + str(data["playerData"]["balancePlayer"]))
                    data["playerData"]["balancePlayer"] = data["playerData"]["balancePlayer"] + data["bet"]
                    print("Твой баланс стал: " + str(data["playerData"]["balancePlayer"]))
                    print("-*" * 10 + "-")
                    WorkWithJSON().WriteFile(data)
                    in_game = False

        if in_game:
            if GameHistory().get_player_points() > GameHistory().get_dealer_points():
                print("Ты выиграл")
                print("-*" * 10 + "-")
                print("Твой баланс был: " + str(data["playerData"]["balancePlayer"]))
                data["playerData"]["balancePlayer"] = data["playerData"]["balancePlayer"] + data["bet"]
                print("Твой баланс стал: " + str(data["playerData"]["balancePlayer"]))
                print("-*" * 10 + "-")
                WorkWithJSON().WriteFile(data)

            else:
                print("Дилер выиграл")
                print("-*" * 10 + "-")
                print("Твой баланс был: " + str(data["playerData"]["balancePlayer"]))
                data["playerData"]["balancePlayer"] = data["playerData"]["balancePlayer"] - data["bet"]
                print("Твой баланс стал: " + str(data["playerData"]["balancePlayer"]))
                WorkWithJSON().WriteFile(data)
                print("-*" * 10 + "-")



if __name__ == "__main__":
    gam = Game()
    gam.new_game()

