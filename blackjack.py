#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

from Hand import *
from Deck import *


class Game:
    def new_game(self):
        history = GameHistory()
        reading = WorkWithJson()
        data = reading.open_file()
        number_of_zeroes = 0
        for key in data["game"]:
            if data["game"][key] == 1:
                query = input("Желаете продолжить игру с предыдущего момента? (y/n) \n")
                if query == 'y':
                    if data["game"]["bet"] == 1:
                        history.get_information()
                        self.run_game(0)

                    if data["game"]["your_game"] == 1:
                        history.get_information()
                        self.run_game(1)

                    if data["game"]["dealer_game"] == 1:
                        history.get_information()
                        self.run_game(2)

                    if data["game"]["comparison"] == 1:
                        history.get_information()
                        self.run_game(3)

                if query == 'n':
                    history.clean()
                    self.authorization()
            if data["game"][key] == 0:
                number_of_zeroes = number_of_zeroes + 1
                if number_of_zeroes == 4:
                    self.authorization()

    def authorization(self):
        reading = WorkWithJson()
        data = reading.open_file()
        history = GameHistory()

        while True:
            if data["player_data"]["namePlayer"] is not None:
                answer_to_the_question = int(input(
                    "Добро пожаловать, выберите пользователя:\n1 Продолжить игру"
                    "\n2 Создать нового пользователя\n3 Вывести статистику игрока \nВвод: "))

                if answer_to_the_question == 1:
                    history.get_player_statistics()

                    dct = WorkWithJson().open_file()
                    history.clean()
                    WorkWithJson().write_file(dct)
                    self.bet()

                if answer_to_the_question == 2:
                    history.create_user()
                    continue

                if answer_to_the_question == 3:
                    history.get_player_statistics()
                    continue

            else:
                while True:
                    answer_to_the_question = int(input(
                        "Добро пожаловать в игру !\n1 Создать нового пользователя"
                        "\n2 Выход\n\nВвод: "))
                    if answer_to_the_question == 1:
                        history.create_user()
                        print("\nНачать игру? (y/n)")
                        answer = history.yes_or_no_question()
                        if answer == 'y':
                            print("\n", "*"*20, "\n")
                            self.bet()
                        if answer == 'n':
                            break
                    break
            break   # end of main loop

    def bet(self):
        history = GameHistory()
        print("На вашем счету " + str(history.get_balance()) + "$")
        history.state_of_the_bet(history.place_a_bet())
        history.states(0)
        self.run_game(0)

    @staticmethod
    def run_game(state):
        history = GameHistory()
        reading = WorkWithJson()
        player_hand = Hand("Игрок")
        dealer_hand = Hand("Дилер")
        d = Deck()
        if state == 0:
            player_hand.add_card(d.deal_card())

            player_hand.add_card(d.deal_card())

            dealer_hand.add_card(d.deal_card())

            print(dealer_hand)
            print("=" * 20)

            print(player_hand)
            history.states(1)
            state = 1
        if state == 1:
            in_game = True
            print("state 1")
            while history.get_player_points() < 21 and history.get_player_points() != 0:
                while True:
                    print(history.get_player_points())
                    query = input("Идти дальше? (y/n) \n")
                    ans = query[0].lower()
                    print(ans)
                    if query == '' or ans not in ['y', 'n']:
                        print('Пожалуйста ответьте y или n!')
                    else:
                        break

                if ans == "y":
                    player_hand.add_card(d.deal_card())
                    print(player_hand)

                    if history.get_player_points() > 21:
                        print("Дилер выиграл")
                        history.change_number_of_losers()
                        dct = reading.open_file()
                        dct["game"]["your_game"] = 0
                        WorkWithJson().write_file(dct)

                        history.get_statistics_at_the_end_of_the_game()

                        in_game = False
                        history.change_player_balance_in_minus(history.get_bet())

                        history.states(9)
                else:
                    print("Ты стоишь!")
                    state = 2
                    history.states(2)
                    break

            if state == 2:
                print("=" * 20)
                print("state2")
                if in_game:
                    while history.get_dealer_points() < 17:
                        dealer_hand.add_card(d.deal_card())
                        print(history.get_dealer_points())
                        print(dealer_hand)
                        if history.get_dealer_points() > 21:
                            print("Ты выиграл")
                            history.change_player_balance_in_plus(history.get_bet())
                            history.change_number_of_wins()
                            history.get_statistics_at_the_end_of_the_game()
                            history.clean()
                            history.states(9)
                            in_game = False

            state = 3
            history.states(3)

            if state == 3:
                print("state3")
                if in_game:
                    if history.get_player_points() > history.get_dealer_points():
                        print("Ты выиграл")
                        history.change_number_of_wins()
                        history.change_player_balance_in_plus(history.get_bet())
                        history.clean()
                        history.get_statistics_at_the_end_of_the_game()
                        history.states(9)
                    else:
                        print("Дилер выиграл")
                        print(dealer_hand)
                        history.change_player_balance_in_minus(GameHistory().get_bet())
                        history.change_number_of_losers()
                        history.get_statistics_at_the_end_of_the_game()
                        history.clean()
                        history.states(9)


if __name__ == "__main__":
    gam = Game()
    gam.new_game()
