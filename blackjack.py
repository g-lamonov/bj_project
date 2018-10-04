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
        if (self.rank) in ('Валет', 'Королева', 'Король', 'Туз'):
            return 10
        else:
            return ('', 'Туз', '2', '3', '4', '5', '6', '7', '8', '9', '10').index(self.rank)

    def get_rank(self):
        return self.rank

    def __str__(self):
        return "%s%s" % (self.rank, self.suit)


class BankAccount:
    def __init__(self):
        self.initial_balance = 500
        self.bet = 0

    def money_of_the_winner(self, amount):
        self.initial_balance += amount
        return self.initial_balance

    def bet_of_player(self, player_bet):
        if int(player_bet) > self.initial_balance:
            print("Cумма ставки превышает баланс")
            return self.bet
        if int(player_bet) < self.initial_balance:
            self.initial_balance -= int(player_bet)
            return self.bet

    def money_of_the_bank_account(self, amount):
        self.initial_balance -= int(amount)
        return self.initial_balance

    def change_hand_player(self):
        return self.initial_balance


class Deck(object):
    def __init__(self):
        ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Валет', 'Королева', 'Король', 'Туз')
        suits = ('♦', '♥', '♣', '♠')
        self.cards = [Card(r, s) for r in ranks for s in suits]
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
        dct = WorkWithJson().open_file()
        while True:
            if self.name == "Игрок":
                lis = dct["player_hand"]
                print(lis)
                lis.append(str(card))
                print(lis)
                break
            if self.name == "Дилер":
                lis = dct["dealer_hand"]
                print(lis)
                lis.append(str(card))
                print(lis)
                break

        if self.name == "Игрок":
            GameHistory().change_hand_player(lis)

        if self.name == "Дилер":
            GameHistory().change_dealer_player(lis)

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
            for card in (GameHistory().player_hand()):
                text += str(card) + " "
            text += "\nЗначение на руке: " + str(self.get_value())
            return text
        if self.name == "Дилер":
            text = "%s содержит :\n" % self.name
            for card in (GameHistory().dealer_hand()):
                text += str(card) + " "
            text += "\nЗначение на руке: " + str(self.get_value())
            return text


class Account:
    def __init__(self, id, name_player, balance):
        self.id = id
        self.name = name_player
        self.balance = balance

    def has_id(self, target_id):
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


class WorkWithJson:

    def open_file(self):
        with open('gameHistory.json', 'r') as f:
            data = json.loads(f.read())
            return data

    def write_file(self, data):
        with open('gameHistory.json', 'w') as f:
            json.dump(data, f)


class GameHistory:
    def change_hand_player(self, data):
        dct = WorkWithJson().open_file()
        dct["player_hand"] = data
        WorkWithJson().write_file(dct)

    def change_dealer_player(self, data):
        dct = WorkWithJson().open_file()
        dct["dealer_hand"] = data
        WorkWithJson().write_file(dct)

    def player_hand(self):
        dct = WorkWithJson().open_file()
        handP = dct["player_hand"]

        return handP

    def dealer_hand(self):
        dct = WorkWithJson().open_file()
        handP = dct["dealer_hand"]

        return handP

    def json_name(self):
        dct = WorkWithJson().open_file()
        name = dct["player_data"]["namePlayer"]
        return name

    def edit_player_data(self, id, namePlayer, balance_player):
        dct = WorkWithJson().open_file()
        dct["player_data"]["id"] = id
        dct["player_data"]["namePlayer"] = namePlayer
        dct["player_data"]["balance_player"] = balance_player
        WorkWithJson().write_file(dct)

    def edit_player_wins(self, result):
        dct = WorkWithJson().open_file()
        i = dct["statistics"]["number_of_wins"]
        i = i + result
        dct["statistics"]["number_of_losers"] = i
        WorkWithJson().write_file(dct)

    def edit_player_losers(self, result):
        dct = WorkWithJson().open_file()
        i = dct["statistics"]["number_of_losers"]
        i = i + result
        dct["statistics"]["number_of_losers"] = i
        WorkWithJson().write_file(dct)

    def state_of_the_bet(self, bet):
        dct = WorkWithJson().open_file()
        dct["bet"] = bet
        WorkWithJson().write_file(dct)

    def get_balance(self):
        dct = WorkWithJson().open_file()
        balance = dct["player_data"]["balance_player"]
        return balance

    def get_player_points(self):
        dct = WorkWithJson().open_file()
        points = dct["player_points"]
        return points

    def change_player_points(self, data):
        dct = WorkWithJson().open_file()
        dct["player_points"] = data
        WorkWithJson().write_file(dct)

    def get_dealer_points(self):
        dct = WorkWithJson().open_file()
        points = dct["dealer_points"]
        return points

    def change_dealer_points(self, data):
        dct = WorkWithJson().open_file()
        dct["dealer_points"] = data
        WorkWithJson().write_file(dct)

    def change_number_of_wins(self):
        dct = WorkWithJson().open_file()
        dct["statistics"]["number_of_wins"] = dct["statistics"]["number_of_wins"] + 1
        WorkWithJson().write_file(dct)

    def change_number_of_losers(self):
        dct = WorkWithJson().open_file()
        dct["statistics"]["number_of_losers"] = dct["statistics"]["number_of_losers"] + 1
        
        WorkWithJson().write_file(dct)
    def new_game(self):
        dct = {"game": {"state1": 0, "state2": 0, "state3": 0, "state4": 0,
                        "state5": 0, "state6": 0, "state7": 0, "state8": 0},
                         "player_data": {"id": None, "namePlayer": None, "balance_player": 5000},
                         "player_hand": [],
                         "dealer_hand": [],
                         "statistics": {"number_of_wins": 0, "number_of_losers": 0},
                         "bet": 0, "player_points": 0,
                         "dealer_points": 0}

        with open('gameHistory.json', 'w+') as file:
            json.dump(dct, file)

    def add_card1(self, card):
        dct = WorkWithJson().open_file()
        cardItems = list(dct["player_hand"])
        cardItems.append(card)
        dct["player_hand"] = cardItems
        WorkWithJson().write_file(dct)


class Game():

    def new_game(self):
        reading = WorkWithJson()
        data = reading.open_file()
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
        reading = WorkWithJson()
        data = reading.open_file()

        while True:
            answer_to_the_question = int(input(
                "Добро пожаловать, выберите пользователя:\n1 Продолжить игру"
                "\n2 Создать нового пользователя\n3 Вывести статистику игрока \nВвод: "))

            if answer_to_the_question == 1:
                player_data = (data["player_data"]["id"],
                               data["player_data"]["namePlayer"],
                               data["player_data"]["balance_player"])
                print(player_data)
                dct = WorkWithJson().open_file()
                dct["player_hand"] = []
                dct["dealer_hand"] = []
                dct["player_points"] = 0
                dct["dealer_points"] = 0
                WorkWithJson().write_file(dct)
                self.run_game()
                break

            if answer_to_the_question == 2:
                print('Создание нового пользователя:\n')
                answer_id = int(input("Введите ID пользователя: "))
                print(answer_id)
                answer_name = input('Введите имя пользователя: ')
                print(answer_name)
                answer_init_balance = int(input('Введите начальный баланс пользователя: '))
                print(answer_init_balance)
                GameHistory().edit_player_data(answer_id, answer_name, answer_init_balance)

                continue

            if answer_to_the_question == 3:
                with open('gameHistory.json', 'r') as f:
                    data = json.loads(f.read())

                    userInformation = (data["player_data"]["id"],
                                       data["player_data"]["namePlayer"],
                                       data["player_data"]["balance_player"],
                                       data["statistics"]["number_of_wins"],
                                       data["statistics"]["number_of_losers"])
                    templateForTheUser = ("ID: %s\n"
                                          "Имя: %s\n"
                                          "Баланс: %d\n"
                                          "Количество побед: %d\n"
                                          "Количество проигрышей: %d\n")
                    print(templateForTheUser % userInformation)
                continue

    def run_game(self):
        reading = WorkWithJson()
        data = reading.open_file()

        player_hand = Hand("Игрок")
        dealer_hand = Hand("Дилер")

        print("You have " + str(GameHistory().get_balance()) + "$ money")

        GameHistory().state_of_the_bet(int(input("Сделайте ставку \n")))
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
                    GameHistory().change_number_of_losers()
                    print("-" * 20)
                    print("Твой баланс был: " + str(data["player_data"]["balance_player"]))
                    data["player_data"]["balance_player"] = data["player_data"]["balance_player"] - data["bet"]
                    print("Твой баланс стал: " + str(data["player_data"]["balance_player"]))
                    print("-" * 20)
                    WorkWithJson().write_file(data)

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
                    print("Твой баланс был: " + str(data["player_data"]["balance_player"]))
                    data["player_data"]["balance_player"] = data["player_data"]["balance_player"] + data["bet"]
                    print("Твой баланс стал: " + str(data["player_data"]["balance_player"]))
                    print("-*" * 10 + "-")
                    WorkWithJson().write_file(data)
                    GameHistory().change_number_of_losers()
                    in_game = False

        if in_game:
            if GameHistory().get_player_points() > GameHistory().get_dealer_points():
                print("Ты выиграл")
                GameHistory().change_number_of_wins()
                print("-*" * 10 + "-")
                print("Твой баланс был: " + str(data["player_data"]["balance_player"]))
                data["player_data"]["balance_player"] = data["player_data"]["balance_player"] + data["bet"]
                print("Твой баланс стал: " + str(data["player_data"]["balance_player"]))
                print("-*" * 10 + "-")
                WorkWithJson().write_file(data)

            else:
                print("Дилер выиграл")
                GameHistory().change_number_of_losers()
                print("-*" * 10 + "-")
                print("Твой баланс был: " + str(data["player_data"]["balance_player"]))
                data["player_data"]["balance_player"] = data["player_data"]["balance_player"] - data["bet"]
                print("Твой баланс стал: " + str(data["player_data"]["balance_player"]))
                WorkWithJson().write_file(data)
                print("-*" * 10 + "-")


if __name__ == "__main__":
    gam = Game()
    gam.new_game()

