import random


def rps():
    hands = ["камень", "ножницы", "бумага"]
    win_hands = {"камень": "ножницы",
                 "ножницы": "бумага",
                 "бумага": "камень",
                 }

    while True:
        bot_hand = random.choice(hands)
        # Меню
        print("1 - камень")
        print("2 - ножницы")
        print("3 - бумага")
        user_hand = input("Введите номер: ")
        # Проверка введенных данных
        if len(user_hand) != 1:
            print("Необходимо вводить одну цифру!")
            continue
        if user_hand not in "123":
            print("Допустимые значения: 1, 2 ,3")
            continue
        if user_hand.isdecimal():
            user_hand = int(user_hand)
        else:
            print("Необходимо вводить только цифры!")
            continue

        print(f"Bot: {bot_hand}, You: {hands[user_hand - 1]}")
        if win_hands[bot_hand] == hands[user_hand - 1]:
            print("Bot win")
        elif bot_hand == hands[user_hand - 1]:
            print("Ничья")
        else:
            print("You win!")
        if input("Еще играем? 1-Да, 0-нет: ") == "1":
            continue
        else:
            break


if __name__ == "__main__":
    rps()
