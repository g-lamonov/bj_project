#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

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

class bankAccount:
    def __init__(self):
        self.initial_balance = 500

    def moneyOfTheWinner(self, amount):
        self.balance +=amount
        return self.initial_balance

    def moneyOfTheBankAccount(self, amount):
        self.balance -= amount
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

from random import shuffle
def new_game():
    file_save = open('21.txt', 'w')
    d = Deck()

    player_balance = bankAccount()
    player_hand = Hand("Игрок")
    dealer_hand = Hand("Дилер")

    print("You have " + str(player_balance.stateOfAnAccount()) + "$ money")

    while True:
        betOfMoney = raw_input("Сделайте ставку \n")
        if betOfMoney > str(player_balance.stateOfAnAccount()):
            print('Ставка превышает баланс!')
        else:
            break

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
            query = raw_input("Идти дальше? (y/n) \n")
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


    print "=" * 20
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


new_game()
