import random


def students_from_file():
    filename = input("Введите название файла: ")
    with open(filename, "r", encoding="utf-8") as file:
        all_students = []
        for i in all_students:
            all_students.append(i.strip())

    return all_students

def students_from_console():
    pass


def students_choicer():
    print("Привет. Это рандомайзер выбора студента!")
    print("Список студентов будет заполнен сейчас или взят из файла?")
    while True:
        print("1. Заполнен сейчас")
        print("2. Взят из файла")
        user_choice = input("Ваш выбор: ")
        if user_choice not in ("1", "2"):
            print("Неизветсная команда. Попробуйте ещё раз")
            continue
        if user_choice == "1":
            all_students = students_from_console()
        else:
            all_students = students_from_file()


        break


if __name__ == "__main__":
    pass
