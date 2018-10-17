from WorkWithJson import *


class GameHistory:
    def create_user(self):
        print('Создание нового пользователя:\n')
        answer_id = int(input("Введите ID пользователя: "))
        print(answer_id)
        answer_name = input('Введите имя пользователя: ')
        print(answer_name)
        answer_init_balance = int(input('Введите начальный баланс пользователя: '))
        print(answer_init_balance)
        self.edit_player_data(answer_id, answer_name, answer_init_balance)
        self.new_game()

    @staticmethod
    def get_player_statistics():
        with open('gameHistory.json', 'r') as f:
            data = json.loads(f.read())

            user_information = (data["player_data"]["id"],
                                data["player_data"]["namePlayer"],
                                data["player_data"]["balance_player"],
                                data["number_of_wins"],
                                data["number_of_losers"])
            template_for_the_user = ("ID: %s\n"
                                     "Имя: %s\n"
                                     "Баланс: %d\n"
                                     "Количество побед: %d\n"
                                     "Количество проигрышей: %d\n")
            print(template_for_the_user % user_information)

    @staticmethod
    def change_hand_player(data):
        dct = WorkWithJson().open_file()
        dct["player_hand"] = data
        WorkWithJson().write_file(dct)

    @staticmethod
    def change_dealer_player(data):
        dct = WorkWithJson().open_file()
        dct["dealer_hand"] = data
        WorkWithJson().write_file(dct)

    @staticmethod
    def player_hand():
        dct = WorkWithJson().open_file()
        hand_p = dct["player_hand"]

        return hand_p

    @staticmethod
    def dealer_hand():
        dct = WorkWithJson().open_file()
        hand_p = dct["dealer_hand"]

        return hand_p

    @staticmethod
    def json_name():
        dct = WorkWithJson().open_file()
        name = dct["player_data"]["namePlayer"]
        return name

    @staticmethod
    def edit_player_data(id, namePlayer, balance_player):
        dct = WorkWithJson().open_file()
        dct["player_data"]["id"] = id
        dct["player_data"]["namePlayer"] = namePlayer
        dct["player_data"]["balance_player"] = balance_player
        WorkWithJson().write_file(dct)

    @staticmethod
    def edit_player_wins(result):
        dct = WorkWithJson().open_file()
        i = dct["number_of_wins"]
        i = i + result
        dct["number_of_losers"] = i
        WorkWithJson().write_file(dct)

    @staticmethod
    def edit_player_losers(result):
        dct = WorkWithJson().open_file()
        i = dct["number_of_losers"]
        i = i + result
        dct["number_of_losers"] = i
        WorkWithJson().write_file(dct)

    @staticmethod
    def state_of_the_bet(data):
        dct = WorkWithJson().open_file()
        dct["bet"] = data
        WorkWithJson().write_file(dct)

    def place_a_bet(self):
        while True:
            try:
                user_input = int(input("Сделайте ставку: "))
            except ValueError:
                print("Введенное значение не является числом, сдейте ставку снова!")
                continue
            if user_input > self.get_balance():
                print("Ставка превышает баланс")

            else:
                print("Ставка принята!")
                break
        return user_input

    @staticmethod
    def get_balance():
        dct = WorkWithJson().open_file()
        balance = dct["player_data"]["balance_player"]
        return balance


    def get_player_points(self):
        dct = WorkWithJson().open_file()
        points = dct["player_points"]
        if points > 21:
            aces = 0
            for i in self.player_hand():
                if i[:3] == 'Туз':
                    aces = aces + 1
            points = points - aces*10
            return points
        if points <= 21:
            return points

    @staticmethod
    def check_aces(hand):
        for i in hand:
            print(i)



    @staticmethod
    def get_dealer_points():
        dct = WorkWithJson().open_file()
        points = dct["dealer_points"]
        return points

    @staticmethod
    def get_bet():
        dct = WorkWithJson().open_file()
        bet = dct["bet"]
        return bet

    @staticmethod
    def change_dealer_points(data):
        dct = WorkWithJson().open_file()
        dct["dealer_points"] = data
        WorkWithJson().write_file(dct)

    @staticmethod
    def change_number_of_wins():
        dct = WorkWithJson().open_file()
        dct["number_of_wins"] = dct["number_of_wins"] + 1
        print(dct["number_of_wins"])
        WorkWithJson().write_file(dct)

    @staticmethod
    def change_number_of_losers():
        dct = WorkWithJson().open_file()
        dct["number_of_losers"] = dct["number_of_losers"] + 1
        print(dct["number_of_losers"])
        WorkWithJson().write_file(dct)

    @staticmethod
    def change_player_balance_in_plus(bet):
        dct = WorkWithJson().open_file()
        dct["player_data"]["balance_player"] = dct["player_data"]["balance_player"] + bet
        WorkWithJson().write_file(dct)

    def change_player_balance_in_minus(self, bet):
        dct = WorkWithJson().open_file()
        dct["player_data"]["balance_player"] = dct["player_data"]["balance_player"] - bet
        WorkWithJson().write_file(dct)
        self.check_player_empty_balance()

    def check_player_empty_balance(self):
        if self.get_balance() == 0:
            print("Ты банкрот\nИгра окончена")
            self.delete_user()

    @staticmethod
    def new_game():
        dct = WorkWithJson().open_file()

        dct["number_of_wins"] = 0
        dct["number_of_losers"] = 0
        dct["player_hand"] = []
        dct["dealer_hand"] = []
        dct["player_points"] = 0
        dct["dealer_points"] = 0
        dct["bet"] = 0

        WorkWithJson().write_file(dct)

    @staticmethod
    def clean():
        dct = WorkWithJson().open_file()

        dct["player_hand"] = []
        dct["dealer_hand"] = []
        dct["player_points"] = 0
        dct["dealer_points"] = 0
        dct["game"]["bet"] = 0
        dct["game"]["your_game"] = 0
        dct["game"]["dealer_game"] = 0
        dct["game"]["comparison"] = 0

        WorkWithJson().write_file(dct)

    @staticmethod
    def add_card1(card):
        dct = WorkWithJson().open_file()
        card_items = list(dct["player_hand"])
        card_items.append(card)
        dct["player_hand"] = card_items
        WorkWithJson().write_file(dct)

    def get_information(self):
        print("Карты игрока: ", self.player_hand())
        print("Количество очков игрока : ", self.get_player_points())
        print("Карты дилера: ", self.dealer_hand())
        print("Количество очков дилера : ", self.get_dealer_points())

    @staticmethod
    def get_statistics_at_the_end_of_the_game():
        data = WorkWithJson().open_file()

        print("-*" * 10 + "-")
        print("Количество побед дилера: " + str(data["number_of_losers"]))
        print("Количество побед игрока: " + str(data["number_of_wins"]))
        print("-*" * 10 + "-")

    @staticmethod
    def states(state):
        dct = WorkWithJson().open_file()
        if state == 0:
            dct["game"]["bet"] = 1
            WorkWithJson().write_file(dct)
        if state == 1:
            dct["game"]["bet"] = 0
            dct["game"]["your_game"] = 1
            WorkWithJson().write_file(dct)
        if state == 2:
            dct["game"]["your_game"] = 0
            dct["game"]["dealer_game"] = 1
            WorkWithJson().write_file(dct)
        if state == 3:
            dct["game"]["dealer_game"] = 0
            dct["game"]["comparison"] = 1
            WorkWithJson().write_file(dct)

        if state == 9:
            dct["game"]["bet"] = 0
            dct["game"]["your_game"] = 0
            dct["game"]["dealer_game"] = 0
            dct["game"]["comparison"] = 0
            WorkWithJson().write_file(dct)

    def delete_user(self):
        self.clean()
        dct = WorkWithJson().open_file()
        dct["player_data"]["id"] = None
        dct["player_data"]["namePlayer"] = None
        dct["player_data"]["id"] = None
        dct["number_of_losers"] = 0
        dct["number_of_wins"] = 0
        dct["bet"] = 0
        WorkWithJson().write_file(dct)

    @staticmethod
    def yes_or_no_question():
        query = input("Ответ: ")
        answer = query[0].lower()
        if query == '' or answer not in ['y', 'n']:
            print('Пожалуйста ответьте y или n!')
        else:
            return query
