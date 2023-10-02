import random


def zero_cross():

    def turn_player(pole, ch):
        khod_pla = check_field(pole)[0]
        print(khod_pla)
        khod = input("Make your move :: ")
        n = 0
        if "a" in khod:
            n += 0
            pole[n][int(khod[1])] = ch
        elif "b" in khod:
            n += 1
            pole[n][int(khod[1])] = ch
        else:
            n += 2
            pole[n][int(khod[1])] = ch

    def turn_comp(pole, ch):
        khod_comp = check_field(pole)[1]
        khod_2 = random.choice(khod_comp)
        if (khod_2 >= 0) and (khod_2 < 3):
            pole[0][khod_2] = ch
        elif (khod_2 > 2) and (khod_2 < 6):
            pole[1][khod_2 - 3] = ch
        else:
            pole[2][khod_2 - 6] = ch

    def check_field(lok):
        emp_pl_slots = []
        comp_moves = []
        koul = []
        n = 0
        for k in lok:
            n += 1
            for i in range(len(k)):
                if k[i] == " ":
                    if n == 1:
                        emp_pl_slots.append("a" + str(i))
                        comp_moves.append(i)
                    elif n == 2:
                        emp_pl_slots.append("b" + str(i))
                        comp_moves.append(i + 3)
                    else:
                        emp_pl_slots.append("c" + str(i))
                        comp_moves.append(i + 6)
        koul.append(emp_pl_slots)
        koul.append(comp_moves)
        return koul

    def victory(pole, ch):
        code = 0
        if pole[0] == [ch, ch, ch]:
            code += 1
        elif pole[1] == [ch, ch, ch]:
            code += 1
        elif pole[2] == [ch, ch, ch]:
            code += 1

        elif pole[0][0] == ch and pole[1][0] == ch and pole[2][0] == ch:
            code += 1
        elif pole[0][1] == ch and pole[1][1] == ch and pole[2][1] == ch:
            code += 1
        elif pole[0][2] == ch and pole[1][2] == ch and pole[2][2] == ch:
            code += 1

        elif pole[0][0] == ch and pole[1][1] == ch and pole[2][2] == ch:
            code += 1

        elif pole[0][2] == ch and pole[1][1] == ch and pole[2][0] == ch:
            code += 1

        return code

    def show_field(field):
        n = 0
        for k in field:
            n += 1
            if n == 2:
                print("----------")
            print(k[0], "|", k[1], "|", k[2], "\n")
            if n == 2:
                print("----------")

    def tic_tac_toes():
        field = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        while True:
            pick = input("Pick your warrior: X or O (write letters!!) :: ")
            a = "Oo"
            b = "Xx"
            comp_hero = ""
            pas_s = 0

            if pick in a:
                comp_hero = "X"
                pas_s = 1
            elif pick in b:
                comp_hero = "O"
                pas_s = 1
            else:
                print("Try again!")

            if pick == "o":
                pick = "O"
            elif pick == "x":
                pick = "X"
            else:
                pass

            if pas_s == 1:
                e_or_n = random.randint(1, 2)
                while True:
                    if e_or_n == 1:
                        show_field(field)
                        turn_comp(field, comp_hero)
                        if victory(field, comp_hero) == 1:
                            print("Computer victory")
                            break
                        show_field(field)
                        turn_player(field, pick)
                        if victory(field, pick) == 1:
                            print("Player victory")
                            break
                    else:
                        show_field(field)
                        turn_player(field, pick)
                        if victory(field, pick) == 1:
                            print("Player victory")
                            break
                        show_field(field)
                        turn_comp(field, comp_hero)
                        if victory(field, comp_hero) == 1:
                            print("Computer victory")
                            break
            else:
                return 0

    tic_tac_toes()


zero_cross()
