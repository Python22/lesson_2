from calc import calc_pavel
from calcMihail import calc_mihail
from rps import rps
from students_choicer import students_choicer
from word_searcher import word_searcher
from zero_cross import zero_cross


if __name__ == "__main__":
    print("Привет. Это самая полезная программа в мире.")
    print("Ты можешь выбрать любое из 6 приложений:")
    print("1. Калькулятор от Павла")
    print("2. Калькулятор от Михаила")
    print("3. 'Камень, ножницы, бумага' от Дмитрия")
    print("4. 'Крестики-нолики' от Михаила")
    print("5. 'Рандомайзер выбора студентов' от ...")
    print("6. 'Крестики-нолики' от Максима")
    user_choice = input("Ваш выбор: ")
    match user_choice:
        case "1": calc_pavel()
        case "2": calc_mihail()
        case "3": rps()
        case "4": students_choicer()
        case "5": word_searcher()
        case "6": zero_cross()    
        case _: print("Неизвестная команда.")
