import random
hands = ["камень", "ножницы", "бумага"]
win_hands = {"камень": "ножницы",
             "ножницы": "бумага",
             "бумага": "камень",

             }


while True:
    bot_hand = random.choice(hands)

    print("1 - камень")
    print("2 - ножницы")
    print("3 - бумага")
    user_hand = int(input("Введите номер: "))
    print(f"Bot: {bot_hand}, you: {hands[user_hand-1]}")
    if win_hands[bot_hand] == hands[user_hand-1]:
        print("Bot win", win_hands[bot_hand])
    elif bot_hand == hands[user_hand-1]:
        print("Ничья")
    else:
        print("You win!")





