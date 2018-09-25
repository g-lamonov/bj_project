#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

import json
class GameHistory:
    def __init__(self):
        self.dct = {"game": {"state1": "0", "state2": "0", "state3": "0", "state4": "0"},
                    "action1": {"id": "id", "namePlayer": "Petya", "balancePlayer": "balance"},
                       "action2": {"playerHand": {"1": ["2", "\u2665"], "2": ["7", "\u2663"]}},
                       "action3": {"dealerHand": {"1": ["3", "\u2664"]}}}

    def jsonName(self):
        return self.dct["action1"]["namePlayer"]
    def jsonBalance(self):
        return ("500")

    def new_game():
        dct = {"game": {"state1": 0, "state2": 0, "state3": 0, "state4": 0,
                  "state5": 0, "state6": 0, "state7": 0, "state8": 0},
         "action1": {"id": None, "namePlayer": None, "balancePlayer": None},
         "action2": {"playerHand": None},
         "action3": {"dealerHand": None}}

class Game():

    def new_game(self):

        with open('gameHistory.json', 'r') as f:
            data = json.loads(f.read())

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
                    break

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

