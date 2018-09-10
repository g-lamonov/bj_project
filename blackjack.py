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

    def __str__(self):
        text =  "%sсодержит :\n" % self.name
        for card in self.cards:
            text += str(card) + " "
        text += "\nЗначение на руке: " + str(self.get_value())

        return text

class Deck(object):
    def __init__(self):
        ranks = ('2','3','4','5','6','7','8','9','10','Валет','Королева','Король','Туз')
        suits = ('Бубны','Червы','Трефы','Пики')
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
        if amount > self.balance:
            raise RuntimeError('No action: Amount greater than available balance.')
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

from random import shuffle
def new_game():
    d = Deck()

    data = {'a list': [1, 42, 3.141, 1337, 'help', u'€'],
            'a string': 'bla',
            'another dict': {'foo': 'bar',
                             'key': 'value',
                             'the answer': 42}}

    with open('data.txt', 'w+') as fil:
        json.dump(data, fil)
    game = True
    while True:
        d = Deck()
        bankAcc = BankAccountManager()

        while True:
            answerToTheQuestion = int(input("Добро пожаловать, выберите пользователя:\n1 Вывести список пользователей\n2 Ввести id пользователя\n3 Создать нового пользователя\n4 Выбрать пользователя\n5 Завершить\nВвод: "))
            if answerToTheQuestion == 1:
                for account in (bankAcc.account_list):
                    print(bankAcc.get_account_report(account.id))

                continue
            if answerToTheQuestion == 2:
                print(bankAcc.get_account_report(int(input('Введите Id пользователя: '))))
                continue
            if answerToTheQuestion == 3:
                print('Создание нового пользователя:\n')
                answerId = int(input('Введите ID пользователя: '))
                print(answerId)
                answerName = input('Введите имя пользователя: ')
                print(answerName)
                answerInitBalance = int(input('Введите начальный баланс пользователя: '))
                print(answerInitBalance)
                bankAcc.add_account(answerId, answerName, answerInitBalance)

                continue
            if answerToTheQuestion == 5:
                break
        player_balance = BankAccount()
        player_hand = Hand("Игрок")
        dealer_hand = Hand("Дилер")

        print("You have " + str(player_balance.stateOfAnAccount()) + "$ money")

        while True:
            player_balance.betOfPlayer(input("Сделайте ставку \n"))
            if player_balance.bet > player_balance.stateOfAnAccount():

                print('Ставка превышает баланс!')
                player_balance.bet == 0
                print(player_balance.bet)
                print(player_balance.stateOfAnAccount())
                continue
            else:

                break
        print("You have " + str(player_balance.stateOfAnAccount()) + "$ money")

        player_hand.add_card(d.deal_card())
        player_hand.add_card(d.deal_card())

        dealer_hand.add_card(d.deal_card())

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
                player_hand.add_card(d.deal_card())
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
                dealer_hand.add_card(d.deal_card())
                print(dealer_hand)
                if dealer_hand.get_value() > 21:

                    print("Дилер проиграл")
                    file_save.write("You win")
                    file_save.close()
                    in_game = False
        if in_game:
            if player_hand.get_value() > dealer_hand.get_value():
                print("Ты выиграл")
                file_save.write("You win")
                file_save.close()

            else:
                print("Дилер выиграл")
                file_save.write('Dealer win')
                file_save.close()

        while True:
            query = input("Желаете продолжить игру? (y/n) \n")
            answ = query[0].lower()
            if query == '' or not ans in ['y', 'n']:
                print('Пожалуйста ответьте y или n!')
            else:
                break
        if answ == "y":
            new_game()
        else:
            print("The end")
        exitTheGame = input("Продолжить игру ? (y/n)")
        if exitTheGame == 'n':
            pass
        else:
            break


new_game()
