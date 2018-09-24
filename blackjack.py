#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

import json

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

class Hand(object):
    def __init__(self, name):
        self.name = name
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

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
    def get_cards(self):
        return self.cards

    def __str__(self):

        text =  "%sсодержит :\n" % self.name
        for card in self.cards:
            text += str(card) + " "
        text += "\nЗначение на руке: " + str(self.get_value())

        return text


class Deck(object):
    def __init__(self):
        ranks = ('2','3','4','5','6','7','8','9','10','Валет','Королева','Король','Туз')
        suits = ('♦','♥','♣','♠')
        self.cards = [Card(r,s) for r in ranks for s in suits]
        shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

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
class GameStatus:
    def playerStatus(self, number):
        if number == 1:
            status = {'identification': 1 ,'bet': 0, 'totalOfTheGame': 0}
            self.jsonDump(status)
        if number == 2:
            status = {'identification': 1, 'bet': 1, 'totalOfTheGame': 0}
            self.jsonDump(status)
        if number == 3:
            status = {'identification': 1, 'bet': 1, 'totalOfTheGame': 1}
            self.jsonDump(status)
        if number == 9:
            status = {'identification': 0, 'bet': 0, 'totalOfTheGame': 0}
            self.jsonDump(status)


    def jsonDump(self, data):
        with open('gameStatus.json', 'w+') as file:
            json.dump(data, file)


from random import shuffle


def new_game():

    file_save = open('21.txt', 'w+')
    pack = Deck()
    game = GameStatus()


    bankAcc = BankAccountManager()

    idPlayer = 1
    path = 'data.json'

    with open('gameStatus.json', 'r') as f:
        status = json.loads(f.read())
    if status['identification'] == 1:
        print('Работает')

    while True:
        answerToTheQuestion = int(input(
            "Добро пожаловать, выберите пользователя:\n1 Вывести данные о пользователе"
            "\n2 Продолжить игру\n3 Создать нового пользователя\nВвод: "))
        if answerToTheQuestion == 1:
            with open(path, 'r') as f:
                data = json.loads(f.read())
                jsonName = data['name']
                jsonBalance = data['balance']
                userInformation = (idPlayer, jsonName, jsonBalance)
                templateForTheUser = ("ID: %s\n"
                                 "Name: %s\n"
                                 "Balance: %.02f\n")
                print(templateForTheUser % userInformation)
            continue
        if answerToTheQuestion == 2:
            with open(path, 'r') as f:
                data = json.loads(f.read())

                jsonName = data['name']
                jsonBalance = data['balance']
                dataArr = (idPlayer, jsonName, jsonBalance)
                player_balance = Account(idPlayer, jsonName, jsonBalance)

            break
        if answerToTheQuestion == 3:
            listToJSON = ['id', 'name', 'balance']
            print('Создание нового пользователя:\n')
            answerId = int(input("Введите ID пользователя: "))
            print(answerId)
            answerName = input('Введите имя пользователя: ')
            print(answerName)
            answerInitBalance = int(input('Введите начальный баланс пользователя: '))
            print(answerInitBalance)
            bankAcc.add_account(answerId, answerName, answerInitBalance)
            dataArray = [answerId, answerName, answerInitBalance]
            dataArr = (idPlayer, bankAcc.account_list[0].name, bankAcc.account_list[0].get_balance())
            data = dict(zip(listToJSON, dataArr))

            with open('data.json', 'w+') as fil:
                json.dump(data, fil)
            file_save.writelines("%s\n" % item for item in dataArray)

            continue

    player_hand = Hand("Игрок")
    dealer_hand = Hand("Дилер")


    print("You have " + str(player_balance.get_balance()) + "$ money")

    player_balance.withdraw(int(input("Сделайте ставку \n")))
    game.playerStatus(int('2'))
    print("Ваш баланс " + str(player_balance.get_balance()) + "$ money")

    player_hand.add_card(pack.deal_card())
    dealer_hand.add_card(pack.deal_card())
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
               15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
               27, 28, 29, 30, 31, 32, 33, 34, 35, 36]

    cards2 = [('2', '♦'), ('2', '♥'), ('2', '♣'), ('2', '♠'), ('3', '♦'), ('3', '♥'), ('3', '♣'), ('3', '♠'), ('4', '♦'),
     ('4', '♥'), ('4', '♣'), ('4', '♠'), ('5', '♦'), ('5', '♥'), ('5', '♣'), ('5', '♠'), ('6', '♦'), ('6', '♥'),
     ('6', '♣'), ('6', '♠'), ('7', '♦'), ('7', '♥'), ('7', '♣'), ('7', '♠'), ('8', '♦'), ('8', '♥'), ('8', '♣'),
     ('8', '♠'), ('9', '♦'), ('9', '♥'), ('9', '♣'), ('9', '♠'), ('10', '♦'), ('10', '♥'), ('10', '♣'), ('10', '♠'),
     ('Валет', '♦'), ('Валет', '♥'), ('Валет', '♣'), ('Валет', '♠'), ('Королева', '♦'), ('Королева', '♥'),
     ('Королева', '♣'), ('Королева', '♠'), ('Король', '♦'), ('Король', '♥'), ('Король', '♣'), ('Король', '♠'),
     ('Туз', '♦'), ('Туз', '♥'), ('Туз', '♣'), ('Туз', '♠')]
    users = dict(zip(numbers, cards2))
    with open('example1.json', 'w+') as f:
        f.write(json.dumps(users))

    print(dealer_hand)
    print("="*20)
    print(player_hand)

    in_game = True
    while player_hand.get_value() < 21:
        if ('Туз') in str(dealer_hand):
            print("У дилера туз, хотите ли застраховаться?")

        while True:
            query = input("Идти дальше? (y/n) \n")
            ans = query[0].lower()
            if query == '' or not ans in ['y', 'n']:
                print('Пожалуйста ответьте y или n!')
            else:
                break
        if ans == "y":
            player_hand.add_card(pack.deal_card())
            print(player_hand)
            if player_hand.get_value() > 21:
                print("Ты проиграл")
                in_game = False
        else:
            print("Ты стоишь!")
            break


    print("=" * 20)
    if in_game:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(pack.deal_card())
            print(dealer_hand)
            if dealer_hand.get_value() > 21:

                print("Дилер проиграл")

                file_save.write("You win")
                file_save.close()
                in_game = False

    if in_game:
        if player_hand.get_value() > dealer_hand.get_value():
            print("Ты выиграл")
            data = {"balance" : 600}
            with open('data.json', 'w+') as fil:
                json.dump(data, fil)

            file_save.write("You win")
            file_save.close()

        else:
            print("Дилер выиграл")
            file_save.write('Dealer win')
            file_save.close()

    while True:
        query = input("Желаете продолжить игру? (y/n) \n")
        answ = query[0].lower()
        if query == '' or not answ in ['y', 'n']:
            print('Пожалуйста ответьте y или n!')
        else:
            break
    if answ == "y":
        game.playerStatus(int('9'))
        new_game()

    if answ == 'n':
        print("The end")
    game.playerStatus(int('9'))



new_game()